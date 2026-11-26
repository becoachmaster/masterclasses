"""Construye clases/NNN-slug/presentacion.html a partir de slides/deck.json y los archivos de cada diapositiva.

Tokens automáticos en el orden de deck.json:
  @pilares      Los 3 pilares con el pilar de la clase resaltado (desde conocimiento/pilares.json)
  @repaso       Aprendizajes y frase ancla de la clase anterior (desde su clase.json)
  @seguimiento  Pregunta por el compromiso de la clase anterior
  @plataforma   Invitación a app.becoach.pro (oscura); @plataforma:claro para la versión clara.
                Va en todas las clases con estilo cristal, antes de la frase ancla.

Estilo (campo "estilo" de deck.json):
  "simple"   Sistema BeCoach v2 (desde el 2026-11-26): paleta azul + Brasa, composición centrada, tarjetas
             Mac, vidrio desenfocado y paleta de datos (motor/simple.css). Plantillas en plantillas/slides-simple/.
  "cristal"  Sistema de cristal en tierra y café (clases 005-006). Plantillas en plantillas/slides/.
  (sin campo) Estilo anterior: así las clases 001-004 no cambian si se reconstruyen.

Uso: python scripts/construir_presentacion.py [clase] [--todas] [--muestra] [--catalogo]
  --muestra   construye plantillas/muestra/ (la clase 4 en el estilo de cristal, para copiar de ahí)
  --catalogo  construye plantillas/catalogo-simple.html (plantillas/slides-simple/, estilo simple)
              y plantillas/catalogo.html (plantillas/slides/, sistema de cristal)
Sale con código 2 si hay advertencias de estilo, para que Claude las vea y las corrija.
"""
import argparse
import base64
import re
import sys

from migrar_v1 import a_v2
from _comun import MOTOR, PLANTILLAS, RAIZ, buscar_clase, cargar_clases, clase_anterior, esc, leer_json, pilares, escribir_si_cambia

F = "font-family:'Manrope', Arial, sans-serif"


def slide_pilares(datos):
    tarjetas = ""
    for p in pilares():
        activo = p["id"] == datos.get("pilar")
        fondo, borde = ("#151413", "") if activo else ("#F7F5F1", "border:1px solid #D6CEC3;")
        titulo, texto, icono = ("#F2EEE8", "#B9B1A7", "#FF5A1F") if activo else ("#1A1918", "#5E554D", "#7A5C4A")
        tarjetas += (
            f'<div style="flex:1; display:flex; flex-direction:column; gap:20px; background:{fondo}; {borde} border-radius:16px; padding:48px">'
            f'<x-icon name="{esc(p.get("icono", "Target"))}" style="color:{icono}; width:64px; height:64px"></x-icon>'
            f'<h3 style="font-size:48px; font-weight:700; line-height:1.15; letter-spacing:-1px; color:{titulo}">{esc(p["nombre"])}</h3>'
            f'<p style="font-size:30px; line-height:1.45; color:{texto}">{esc(p.get("descripcion", ""))}</p></div>'
        )
    hoy = next((p["nombre"] for p in pilares() if p["id"] == datos.get("pilar")), None)
    nota = f"Hoy trabajamos el pilar: {hoy}." if hoy else "Esta clase aún no tiene pilar asignado en clase.json."
    return (
        f'<section id="pilares" data-transition="fade" style="background:#ECE7E0; color:#1A1918; {F}; padding:128px; display:flex; flex-direction:column; justify-content:center; gap:64px">'
        '<h2 style="font-size:80px; font-weight:700; line-height:1.08; letter-spacing:-2px">Los 3 pilares del liderazgo personal</h2>'
        f'<div style="display:flex; gap:32px">{tarjetas}</div>'
        f'<aside>APERTURA. Explica en un minuto los tres pilares y ubica a la audiencia. {esc(nota)} La tarjeta oscura es el pilar de hoy.</aside></section>'
    )


def slide_repaso(previa):
    datos = previa[1]
    filas = ""
    for i, a in enumerate(datos.get("aprendizajes", [])[:3], 1):
        filas += (
            '<div style="display:flex; align-items:center; gap:32px; padding:24px 0; border-top:1px solid #CDD3D6">'
            f'<p style="width:64px; font-size:40px; font-weight:800; color:#7A5C4A">{i}</p>'
            f'<p style="flex:1; font-size:38px; font-weight:600; line-height:1.3">{esc(a)}</p></div>'
        )
    ancla = datos.get("frase_ancla", "")
    ancla_html = (f'<p style="font-size:32px; font-style:italic; line-height:1.4; color:#7A5C4A">“{esc(ancla)}”</p>' if ancla else "")
    return (
        f'<section id="repaso" data-transition="fade" style="background:#E6EAEC; color:#1A1918; {F}; padding:128px; display:flex; flex-direction:column; justify-content:start; gap:48px">'
        '<div style="display:flex; flex-direction:column; gap:16px">'
        '<h2 style="font-size:80px; font-weight:700; line-height:1.08; letter-spacing:-2px">Lo que aprendimos la clase anterior</h2>'
        f'<p style="font-size:36px; line-height:1.3; color:#5E554D">{esc(datos.get("titulo", ""))}</p></div>'
        f'<div style="display:flex; flex-direction:column">{filas}</div>{ancla_html}'
        '<aside>APERTURA. Repasa en dos minutos. Pide en el chat: ¿cuál de estos aprendizajes aplicaste esta semana? Para quienes llegan por primera vez, este repaso es la puerta de entrada al hilo del programa.</aside></section>'
    )


def slide_seguimiento(previa):
    compromiso = previa[1].get("compromiso", "")
    return (
        f'<section id="seguimiento" data-transition="fade" style="background:#151413; color:#F2EEE8; {F}; padding:128px; display:flex; flex-direction:column; justify-content:center; align-items:start; gap:48px">'
        '<h2 style="font-size:112px; font-weight:700; line-height:1.05; letter-spacing:-3px">¿Cumpliste tu compromiso?</h2>'
        f'<p style="width:1400px; font-size:44px; line-height:1.35; color:#B9B1A7">{esc(compromiso)}</p>'
        '<aside>APERTURA · SEGUIMIENTO. Pide en el chat: sí, no o a medias. Lee dos o tres historias breves. Si alguien no lo cumplió, no hay juicio: pregunta qué se interpuso. Este momento sostiene el hábito y hace que la gente vuelva.</aside></section>'
    )


# ---------- Diapositivas automáticas en el sistema de cristal ----------
def slide_pilares_cristal(datos):
    tarjetas = ""
    for p in pilares():
        activo = p["id"] == datos.get("pilar")
        clase = "cristal foco" if activo else "cristal"
        icono = "#FF5A1F" if activo else "#C9AC91"
        texto = "#F7F5F1" if activo else "rgba(247,245,241,.68)"
        tarjetas += (
            f'<div class="{clase}" style="flex:1; display:flex; flex-direction:column; gap:24px; padding:52px 48px">'
            f'<x-icon name="{esc(p.get("icono", "Target"))}" style="color:{icono}; width:72px; height:72px"></x-icon>'
            f'<h3 style="font-size:50px; font-weight:800; line-height:1.12; letter-spacing:-1px">{esc(p["nombre"])}</h3>'
            f'<p style="font-size:32px; font-weight:600; line-height:1.4; color:{texto}">{esc(p.get("descripcion", ""))}</p></div>'
        )
    hoy = next((p["nombre"] for p in pilares() if p["id"] == datos.get("pilar")), None)
    nota = f"Hoy trabajamos el pilar: {hoy}." if hoy else "Esta clase aún no tiene pilar asignado en clase.json."
    return (
        f'<section id="pilares" class="fondo" data-transition="fade" style="{F}; padding:96px 110px; display:flex; flex-direction:column; justify-content:space-between">'
        '<h2 style="width:1180px; font-size:84px; font-weight:800; line-height:1.04; letter-spacing:-2.5px">Los 3 pilares del liderazgo personal</h2>'
        f'<div style="display:flex; gap:36px; height:560px">{tarjetas}</div>'
        f'<aside>APERTURA. Explica en un minuto los tres pilares y ubica a la audiencia. {esc(nota)} La tarjeta con borde Brasa es el pilar de hoy.</aside></section>'
    )


def slide_repaso_cristal(previa):
    datos = previa[1]
    filas = ""
    # "repaso": versión corta de los aprendizajes para la pantalla (opcional)
    for i, a in enumerate((datos.get("repaso") or datos.get("aprendizajes", []))[:3], 1):
        filas += (
            '<div class="cristal" style="display:flex; align-items:center; gap:32px; padding:0 40px; height:172px">'
            f'<p style="width:70px; flex:none; font-size:56px; font-weight:800; color:#C9AC91">0{i}</p>'
            f'<p style="font-size:36px; font-weight:700; line-height:1.3">{esc(a)}</p></div>'
        )
    ancla = datos.get("frase_ancla", "")
    ancla_html = (
        '<div class="cristal" style="position:absolute; left:1190px; top:440px; width:620px; height:520px; padding:56px; display:flex; flex-direction:column; justify-content:center">'
        '<p class="serif brillo" style="font-size:180px; line-height:.6; height:80px">“</p>'
        f'<p class="serif" style="margin-top:24px; font-size:54px; line-height:1.18">{esc(ancla)}</p></div>' if ancla else "")
    return (
        f'<section id="repaso" class="fondo-mineral" data-transition="fade" style="{F}">'
        '<div style="position:absolute; left:110px; top:96px; width:1180px; display:flex; flex-direction:column; gap:14px">'
        '<h2 style="font-size:76px; font-weight:800; line-height:1.04; letter-spacing:-2px">Lo que aprendimos la clase anterior</h2>'
        f'<p style="font-size:38px; font-weight:700; color:#C9AC91">{esc(datos.get("titulo", ""))}</p></div>'
        f'<div style="position:absolute; left:110px; top:420px; width:1000px; display:flex; flex-direction:column; gap:24px">{filas}</div>{ancla_html}'
        '<aside>APERTURA. Repasa en dos minutos. Pide en el chat: ¿cuál de estos aprendizajes aplicaste esta semana? Para quienes llegan por primera vez, este repaso es la puerta de entrada al hilo del programa.</aside></section>'
    )


def slide_seguimiento_cristal(previa):
    compromiso = previa[1].get("compromiso", "")
    return (
        f'<section id="seguimiento" class="fondo" data-transition="fade" style="{F}">'
        '<div class="halo" style="left:-200px; top:300px; width:1100px; height:1000px"></div>'
        '<h2 style="position:absolute; left:110px; top:300px; width:1200px; font-size:120px; font-weight:800; line-height:1.02; letter-spacing:-3.5px">¿Cumpliste tu <span class="brillo">compromiso</span>?</h2>'
        f'<div class="cristal" style="position:absolute; left:110px; top:640px; width:1500px; padding:44px 52px; font-size:42px; font-weight:600; line-height:1.35; color:rgba(247,245,241,.85)">{esc(compromiso)}</div>'
        '<aside>APERTURA · SEGUIMIENTO. Pide en el chat: sí, no o a medias. Lee dos o tres historias breves. Si alguien no lo cumplió, no hay juicio: pregunta qué se interpuso. Este momento sostiene el hábito y hace que la gente vuelva.</aside></section>'
    )


def css_estilo(estilo=None, v1=False):
    """CSS del motor según la marca y el estilo.
    v1=True: motor congelado de la marca v1 (tierra y café), solo para las clases ya dictadas (001-006).
    "simple": motor/deck.css completo (base + bloque de marca del manual) + motor/simple.css."""
    css = (MOTOR / ("deck-v1.css" if v1 else "deck.css")).read_text(encoding="utf-8")
    if estilo == "simple" and not v1:
        css += "\n" + (MOTOR / "simple.css").read_text(encoding="utf-8")
    return css


def css_con_fuentes(estilo=None, v1=False):
    """Incrusta motor/fuentes/*.woff2 en el CSS para que la presentación no dependa de internet."""
    css = css_estilo(estilo, v1)
    for fuente in (MOTOR / "fuentes").glob("*.woff2"):
        datos = base64.b64encode(fuente.read_bytes()).decode("ascii")
        css = css.replace(f"url(fuentes/{fuente.name})", f"url(data:font/woff2;base64,{datos})")
    return css


# ---------- @plataforma: la invitación a la plataforma, en todas las clases ----------
PLATAFORMA = {
    "url": "app.becoach.pro",
    "items": [("Todas las clases", "play"), ("Guías prácticas", "guia"), ("Descargables", "bajar")],
    "acceso": "Acceso gratuito",
}
_ICONOS_PLAT = {
    "play": '<circle cx="48" cy="48" r="36"/><path d="M40 33 L64 48 L40 63 Z"/>',
    "guia": '<path d="M18 20h24a8 8 0 0 1 8 8v52a6 6 0 0 0-6-6H18z"/><path d="M78 20H58a8 8 0 0 0-8 8v52a6 6 0 0 1 6-6h22z"/>',
    "bajar": '<path d="M48 14v46"/><path d="M30 44l18 18 18-18"/><path d="M18 74v8h60v-8"/>',
    "check": '<path d="M22 50l16 16 36-36"/>',
}


def _ico(nombre, tam, color):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 96 96" fill="none" stroke="{color}" stroke-width="7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex:none; width:{tam}px; height:{tam}px">{_ICONOS_PLAT[nombre]}</svg>')


def slide_plataforma(datos, claro=False):
    """Invitación a la plataforma con una ventana de navegador que muestra las clases hasta la de hoy."""
    fondo, tarjeta = ("fondo-claro", "claro") if claro else ("fondo", "cristal")
    texto, texto2 = ("#1A1918", "#5E554D") if claro else ("#F7F5F1", "rgba(247,245,241,.68)")
    acento = "#C43A08" if claro else "#C9AC91"
    url_color = "color:#C43A08" if claro else 'color:#FF5A1F; text-shadow:0 0 40px rgba(255,90,31,.45)'
    filas = "".join(
        f'<div class="{tarjeta}" style="display:flex; align-items:center; gap:28px; height:104px; padding:0 32px; border-radius:24px">'
        f'{_ico(ic, 52, acento)}<p style="font-size:40px; font-weight:800; letter-spacing:-.5px">{esc(t)}</p></div>'
        for t, ic in PLATAFORMA["items"])
    # Las clases que ya existen hasta la de hoy, la más reciente primero
    numero = datos.get("numero", 0)
    clases = [d for _, d in cargar_clases() if d.get("numero", 0) <= numero][-4:][::-1] or [datos]
    miniaturas = ""
    for k, d in enumerate(clases):
        hoy = k == 0
        marco = ("brasa" if hoy else tarjeta)
        play_c = "#1A1918" if hoy else acento
        t_c = "#1A1918" if (hoy or claro) else "#F7F5F1"
        miniaturas += (
            f'<div class="{marco}" style="display:flex; flex-direction:column; justify-content:space-between; padding:22px 24px; border-radius:20px; height:230px">'
            f'{_ico("play", 44, play_c)}'
            f'<p style="font-size:24px; font-weight:800; line-height:1.2; color:{t_c}">Clase {d.get("numero", 0)} · {esc(d.get("titulo", ""))}</p></div>')
    barra = "rgba(26,25,24,.06)" if claro else "rgba(255,255,255,.06)"
    return (
        f'<section id="plataforma" class="{fondo}" data-transition="fade" style="{F}">'
        + ("" if claro else '<div class="halo" style="left:-260px; top:120px; width:1200px; height:700px"></div>')
        + f'<h2 style="position:absolute; left:110px; top:290px; width:1000px; font-size:112px; font-weight:800; letter-spacing:-4px; line-height:1; {url_color}">{esc(PLATAFORMA["url"])}</h2>'
        f'<div style="position:absolute; left:110px; top:470px; width:860px; display:flex; flex-direction:column; gap:20px">{filas}</div>'
        f'<div style="position:absolute; left:110px; top:870px; display:flex; align-items:center; gap:18px; padding:20px 34px; border-radius:22px; '
        f'background:{"#1A1918" if claro else "rgba(63,125,92,.18)"}; border:1px solid {"#1A1918" if claro else "rgba(120,190,150,.45)"}">'
        f'{_ico("check", 44, "#9BD3B0")}<p style="font-size:40px; font-weight:800; color:#F7F5F1">{esc(PLATAFORMA["acceso"])}</p></div>'
        # Ventana de navegador (debajo de la zona de la cámara)
        f'<div class="{tarjeta}" style="position:absolute; left:1080px; top:380px; width:730px; height:600px; padding:0; overflow:hidden">'
        f'<div style="display:flex; align-items:center; gap:12px; height:72px; padding:0 26px; background:{barra}; border-bottom:1px solid {barra}">'
        '<div style="width:16px; height:16px; border-radius:50%; background:#FF5A1F"></div>'
        f'<div style="width:16px; height:16px; border-radius:50%; background:{acento}; opacity:.7"></div>'
        f'<div style="width:16px; height:16px; border-radius:50%; background:{acento}; opacity:.4"></div>'
        f'<p style="margin-left:18px; flex:1; padding:6px 20px; border-radius:12px; background:{barra}; font-size:24px; font-weight:700; color:{texto2}">{esc(PLATAFORMA["url"])}</p></div>'
        f'<div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; padding:28px">{miniaturas}</div></div>'
        '<aside>PLATAFORMA. Cuenta que todas las clases quedan grabadas y ordenadas por partes en app.becoach.pro, con guías prácticas y descargables, y que el acceso es gratuito. Pide que entren hoy y vean la parte de esta clase que más les sirvió. Deja el enlace en el chat.</aside></section>'
    )


# ---------- Diapositivas automáticas en el estilo simple (sistema v2) ----------


def slide_pilares_simple(datos):
    tarjetas = ""
    for i, p in enumerate(pilares(), 1):
        activo = p["id"] == datos.get("pilar")
        tarjetas += (
            f'<div class="card center{" foco" if activo else ""} rise" style="--i:{i}; padding:48px 36px; gap:18px">'
            f'<div class="badge{" brasa-b" if activo else ""}"><x-icon name="{esc(p.get("icono", "Target"))}" style="width:44px; height:44px"></x-icon></div>'
            f'<h3>{esc(p["nombre"])}</h3>'
            f'<p class="small"{" style=\"color:#141B2D\"" if activo else ""}>{esc(p.get("descripcion", ""))}</p></div>')
    hoy = next((p["nombre"] for p in pilares() if p["id"] == datos.get("pilar")), None)
    nota = f"Hoy trabajamos el pilar: {hoy}." if hoy else "Esta clase aún no tiene pilar asignado en clase.json."
    pill = f'<p class="pill soft rise" style="--i:4">Hoy trabajamos {esc(hoy)}</p>' if hoy else ""
    return (
        f'<section id="pilares" class="s" data-transition="fade" style="{F}"><div class="puntos"></div>'
        '<h2 class="rise" style="--i:0">Los 3 pilares del liderazgo personal</h2>'
        f'<div class="grid3">{tarjetas}</div>{pill}'
        f'<aside>APERTURA. Explica en un minuto los tres pilares y ubica a la audiencia. {esc(nota)} La tarjeta con borde Brasa es el pilar de hoy.</aside></section>')


def slide_repaso_simple(previa):
    datos = previa[1]
    tarjetas = ""
    for i, a in enumerate((datos.get("repaso") or datos.get("aprendizajes", []))[:3], 1):
        tarjetas += (f'<div class="card vidrio rise" style="--i:{i}; gap:18px; padding:36px 40px"><div class="badge">{i}</div>'
                     f'<p style="font-size:34px; font-weight:700; line-height:1.3">{esc(a)}</p></div>')
    ancla = datos.get("frase_ancla", "")
    ancla_html = (f'<div class="card vidrio center rise" style="--i:4; width:1560px; padding:30px 48px">'
                  f'<p class="serif" style="font-size:46px; line-height:1.2">«{esc(ancla)}»</p></div>') if ancla else ""
    return (
        f'<section id="repaso" class="s" data-transition="fade" style="{F}; gap:36px"><div class="puntos"></div>'
        '<h2 class="rise" style="--i:0">Lo que aprendimos la clase anterior</h2>'
        f'<p class="pill soft rise" style="--i:0">{esc(datos.get("titulo", ""))}</p>'
        f'<div class="grid3">{tarjetas}</div>{ancla_html}'
        '<aside>APERTURA. Repasa en dos minutos. Pide en el chat: ¿cuál de estos aprendizajes aplicaste esta semana? Para quienes llegan por primera vez, este repaso es la puerta de entrada al hilo del programa.</aside></section>')


def slide_seguimiento_simple(previa):
    compromiso = previa[1].get("compromiso", "")
    return (
        f'<section id="seguimiento" class="s az" data-transition="fade" style="{F}"><div class="puntos"></div>'
        '<h2 class="rise" style="--i:0; font-size:96px; max-width:800px">¿Cumpliste tu <span class="foco-t">compromiso</span>?</h2>'
        f'<div class="card vidrio center rise" style="--i:1; width:1400px; padding:40px 56px"><p style="font-size:40px; font-weight:600; line-height:1.35">{esc(compromiso)}</p></div>'
        '<div class="row rise" style="--i:2; gap:20px"><p class="pill white">Sí</p><p class="pill white">No</p><p class="pill white">A medias</p></div>'
        '<aside>APERTURA · SEGUIMIENTO. Pide en el chat: sí, no o a medias. Lee dos o tres historias breves. Si alguien no lo cumplió, no hay juicio: pregunta qué se interpuso. Este momento sostiene el hábito y hace que la gente vuelva.</aside></section>')


def slide_plataforma_simple(datos):
    items = "".join(
        f'<div class="card rise" style="--i:{k + 1}; flex-direction:row; align-items:center; gap:24px; padding:22px 30px">'
        f'<div class="badge" style="width:64px; height:64px">{_ico(ic, 34, "#FFFFFF")}</div>'
        f'<p style="font-size:34px; font-weight:800">{esc(t)}</p></div>' for k, (t, ic) in enumerate(PLATAFORMA["items"]))
    numero = datos.get("numero", 0)
    clases = [d for _, d in cargar_clases() if d.get("numero", 0) <= numero][-4:][::-1] or [datos]
    minis = "".join(
        f'<div class="card{" brasac" if k == 0 else ""}" style="padding:20px 22px; gap:10px; height:190px; justify-content:space-between">'
        f'{_ico("play", 40, "#141B2D" if k == 0 else "#3D5A8C")}'
        f'<p style="font-size:24px; font-weight:800; line-height:1.2">Clase {d.get("numero", 0)} · {esc(d.get("titulo", ""))}</p></div>'
        for k, d in enumerate(clases))
    return (
        f'<section id="plataforma" class="s" data-transition="fade" style="{F}; gap:40px"><div class="puntos"></div>'
        f'<h2 class="rise" style="--i:0; color:#1E2A4E">{esc(PLATAFORMA["url"])}</h2>'
        '<div class="row" style="gap:48px; align-items:stretch">'
        f'<div class="col" style="width:620px; gap:20px">{items}<p class="pill rise" style="--i:4; align-self:flex-start">✓ {esc(PLATAFORMA["acceso"])}</p></div>'
        '<div class="card vidrio rise" style="--i:2; width:840px; padding:0; gap:0; overflow:hidden">'
        '<div class="row" style="justify-content:flex-start; gap:12px; height:64px; padding:0 24px; border-bottom:1px solid rgba(61,90,140,.15)">'
        '<span style="width:14px; height:14px; border-radius:50%; background:#FF5A1F"></span><span style="width:14px; height:14px; border-radius:50%; background:#A9BEE0"></span><span style="width:14px; height:14px; border-radius:50%; background:#DCE4F0"></span>'
        f'<p style="margin-left:14px; font-size:24px; font-weight:700; color:#4E5A70">{esc(PLATAFORMA["url"])}</p></div>'
        f'<div class="grid2" style="width:auto; gap:18px; padding:24px">{minis}</div></div></div>'
        '<aside>PLATAFORMA. Cuenta que todas las clases quedan grabadas y ordenadas por partes en app.becoach.pro, con guías prácticas y descargables, y que el acceso es gratuito. Pide que entren hoy y vean la parte de esta clase que más les sirvió. Deja el enlace en el chat.</aside></section>')


PATRONES_PROHIBIDOS = [
    (r"\ben el chat\b", "indicación de chat en pantalla"),
    (r"\bencuesta\b", "indicación de encuesta en pantalla"),
    (r"\b\d+\s*(min|minutos)\b", "marca de tiempo en pantalla"),
    (r"\bfase \d+ de \d+\b", "fase con numeración de ejercicio en pantalla"),
]


def revisar(id_slide, html):
    avisos = []
    visible = re.sub(r"<aside>.*?</aside>", " ", html, flags=re.S | re.I)
    texto = re.sub(r"<[^>]+>", " ", visible)
    for patron, motivo in PATRONES_PROHIBIDOS:
        if re.search(patron, texto, re.I):
            avisos.append(f"{id_slide}: {motivo} ('{re.search(patron, texto, re.I).group(0)}'). Muévelo a las notas.")
    for m in re.finditer(r'<p style="([^"]*)">[^<]{1,80}</p>\s*<h[1-3]', visible, re.I):
        estilo = m.group(1).replace(" ", "").lower()
        if "text-transform:uppercase" in estilo and "position:absolute" not in estilo:
            avisos.append(f"{id_slide}: parece un pretítulo encima de un título. Quítalo.")
            break
    if "<aside>" not in html:
        avisos.append(f"{id_slide}: no tiene notas del orador (<aside>).")
    if re.search(r'<img[^>]+src="https?://', html):
        avisos.append(f"{id_slide}: imagen remota. Usa archivos locales en recursos/ o SVG en línea.")
    for m in re.finditer(r"font-size:\s*(\d+)px", visible):
        if int(m.group(1)) < 24:
            avisos.append(f"{id_slide}: texto de {m.group(1)}px. El mínimo es 24px.")
            break
    return avisos


def construir(carpeta, datos):
    deck = leer_json(carpeta / "slides" / "deck.json")
    orden = deck.get("orden") or deck.get("order") or []
    previa = clase_anterior(datos.get("numero", 0))
    estilo = deck.get("estilo")
    simple = estilo == "simple"
    cristal = estilo == "cristal"
    # Marca: "v1" (tierra y café) solo en las clases dictadas antes del 2026-11-26; todas las demás, manual v2 (azul).
    v1 = deck.get("marca") == "v1"
    partes, avisos = [], []
    for id_slide in orden:
        if id_slide in ("@plataforma", "@plataforma:claro"):
            partes.append(slide_plataforma_simple(datos) if simple else slide_plataforma(datos, claro=id_slide.endswith(":claro")))
        elif id_slide == "@pilares":
            partes.append(slide_pilares_simple(datos) if simple else slide_pilares_cristal(datos) if cristal else slide_pilares(datos))
        elif id_slide in ("@repaso", "@seguimiento"):
            if not previa:
                avisos.append(f"{id_slide}: no hay clase anterior; se omite.")
                continue
            if id_slide == "@repaso" and not previa[1].get("aprendizajes"):
                avisos.append("@repaso: la clase anterior no tiene aprendizajes. Ciérrala con /cerrar-clase.")
            if id_slide == "@seguimiento" and not previa[1].get("compromiso"):
                avisos.append("@seguimiento: la clase anterior no tiene compromiso registrado.")
            if simple:
                partes.append(slide_repaso_simple(previa) if id_slide == "@repaso" else slide_seguimiento_simple(previa))
            elif cristal:
                partes.append(slide_repaso_cristal(previa) if id_slide == "@repaso" else slide_seguimiento_cristal(previa))
            else:
                partes.append(slide_repaso(previa) if id_slide == "@repaso" else slide_seguimiento(previa))
        else:
            archivo = carpeta / "slides" / f"{id_slide}.html"
            if not archivo.exists():
                avisos.append(f"{id_slide}: falta el archivo slides/{id_slide}.html")
                continue
            html = archivo.read_text(encoding="utf-8").strip()
            avisos += revisar(id_slide, html)
            partes.append(html)
    if (cristal or simple) and not any(i.startswith("@plataforma") for i in orden):
        avisos.append("Falta @plataforma (invitación a app.becoach.pro). Ponla antes de la frase ancla; @plataforma:claro si va mejor en claro.")
    en_carpeta = {p.stem for p in (carpeta / "slides").glob("*.html")}
    sueltas = sorted(en_carpeta - set(orden))
    if sueltas:
        avisos.append("Diapositivas que no están en deck.json (no se incluyen): " + ", ".join(sueltas))

    plantilla = (MOTOR / "plantilla.html").read_text(encoding="utf-8")
    titulo = deck.get("titulo") or datos.get("titulo", "Clase")
    salida = (plantilla.replace("{{TITULO}}", esc(titulo))
              .replace("{{CSS}}", css_con_fuentes(estilo, v1))
              .replace("{{JS}}", (MOTOR / "deck.js").read_text(encoding="utf-8"))
              .replace("{{SLIDES}}", diapositivas(partes, v1)))
    escribir_si_cambia(carpeta / "presentacion.html", salida)
    return len(partes), avisos


def diapositivas(partes, v1=False):
    """Une las diapositivas. En la marca v2 traduce los colores v1 que queden (las automáticas de este script y
    cualquier diapositiva copiada de una clase vieja) con la tabla de migracion (migrar_v1.py, copia de becoach-marca)."""
    html = "\n".join(partes)
    return html if v1 else a_v2(html)[0]


def construir_catalogo(carpeta="slides", estilo=None, nombre="catalogo.html"):
    """Todas las plantillas de una carpeta de plantillas/ en una sola presentación, en orden alfabético."""
    partes, avisos = [], []
    for archivo in sorted((PLANTILLAS / carpeta).glob("*.html")):
        html = archivo.read_text(encoding="utf-8").strip()
        avisos += revisar(archivo.stem, html)
        partes.append(html)
    plantilla = (MOTOR / "plantilla.html").read_text(encoding="utf-8")
    salida = (plantilla.replace("{{TITULO}}", "Catálogo de plantillas")
              .replace("{{CSS}}", css_con_fuentes(estilo))
              .replace("{{JS}}", (MOTOR / "deck.js").read_text(encoding="utf-8"))
              .replace("{{SLIDES}}", diapositivas(partes)))
    escribir_si_cambia(PLANTILLAS / nombre, salida)
    return len(partes), avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("clase", nargs="?")
    ap.add_argument("--todas", action="store_true")
    ap.add_argument("--muestra", action="store_true")
    ap.add_argument("--catalogo", action="store_true")
    a = ap.parse_args()
    if a.catalogo:
        todos = []
        for carpeta, estilo, nombre in (("slides-simple", "simple", "catalogo-simple.html"), ("slides", None, "catalogo.html")):
            n, avisos = construir_catalogo(carpeta, estilo, nombre)
            print(f"plantillas/{nombre} · {n} plantillas")
            todos += avisos
        for aviso in todos:
            print(f"  ⚠ {aviso}", file=sys.stderr)
        sys.exit(2 if todos else 0)
    if a.muestra:
        muestra = PLANTILLAS / "muestra"
        objetivos = [(muestra, leer_json(muestra / "clase.json"))]
    else:
        objetivos = cargar_clases() if a.todas else [buscar_clase(a.clase)]
    if not objetivos or objetivos[0] is None:
        sys.exit("No encontré la clase.")
    hubo_avisos = False
    for carpeta, datos in objetivos:
        if not (carpeta / "slides" / "deck.json").exists():
            continue
        n, avisos = construir(carpeta, datos)
        print(f"{carpeta.relative_to(RAIZ)}/presentacion.html · {n} diapositivas")
        for aviso in avisos:
            hubo_avisos = True
            print(f"  ⚠ {aviso}", file=sys.stderr)
    sys.exit(2 if hubo_avisos else 0)


if __name__ == "__main__":
    main()
