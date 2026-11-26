"""Genera proyecto-claude/: los archivos de conocimiento para el Proyecto de claude.ai (chat).

En el chat no corren scripts ni hooks, así que el paquete deja todo listo para leer:
  01-programa.md                 marco, estructura de clase, pilares, reglas aprendidas y decisiones
  02-diseno.md                   guía de diseño del sistema de cristal
  03-historial.md                bitácora, mapa de temas, glosario e ideas de temas
  04-ultima-clase.md             la última clase completa (ficha + contenido) como referencia
  kit-presentacion.html          el motor (CSS + JS) listo para un artefacto, con diapositivas automáticas de ejemplo
  plantillas-diapositivas.html   todas las plantillas de plantillas/slides/, una tras otra

Uso: python scripts/paquete_proyecto.py
"""
import json
import re

from _comun import CLASES, CONOCIMIENTO, MOTOR, PLANTILLAS, RAIZ, cargar_clases, clase_anterior
import construir_presentacion as cp

SALIDA = RAIZ / "proyecto-claude"
FUENTES_GOOGLE = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
                  '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
                  '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@1,500&family=Manrope:wght@400..800&display=block" rel="stylesheet">')


def leer(ruta):
    return ruta.read_text(encoding="utf-8").strip()


def unir(titulo, partes):
    texto = f"# {titulo}\n\n> Generado por scripts/paquete_proyecto.py. Para cambiarlo, edita los archivos originales del repositorio.\n"
    for nombre, cuerpo in partes:
        texto += f"\n\n---\n\n<!-- Fuente: {nombre} -->\n\n{cuerpo}\n"
    return texto


def css_artefacto():
    css = (MOTOR / "deck.css").read_text(encoding="utf-8")
    return re.sub(r"@font-face\s*\{[^}]*\}\s*", "", css)


def kit(clases):
    carpeta, datos = clases[-1]
    previa = clase_anterior(datos.get("numero", 0))
    slides = [leer(PLANTILLAS / "slides" / "portada.html"), cp.slide_pilares_cristal(datos)]
    if previa:
        slides += [cp.slide_repaso_cristal(previa), cp.slide_seguimiento_cristal(previa)]
    for nombre in ("pregunta", "modelo", "compromiso"):
        slides.append(leer(PLANTILLAS / "slides" / f"{nombre}.html"))
    slides += [cp.slide_plataforma(datos), leer(PLANTILLAS / "slides" / "ancla.html")]
    plantilla = (MOTOR / "plantilla.html").read_text(encoding="utf-8")
    html = (plantilla.replace("{{TITULO}}", "Kit de presentación BeCoach")
            .replace("<style>", FUENTES_GOOGLE + "\n<style>", 1)
            .replace("{{CSS}}", css_artefacto())
            .replace("{{JS}}", (MOTOR / "deck.js").read_text(encoding="utf-8"))
            .replace("{{SLIDES}}", cp.diapositivas(slides)))
    aviso = ("<!--\nKIT DE PRESENTACIÓN BECOACH (sistema de cristal azul, manual de marca v2: https://marca.becoach.pro)\n"
             "Para crear la presentación de una clase como artefacto: copia este archivo COMPLETO (head, <style> y <script>) "
             "y reemplaza solo las <section> dentro de <main id=\"deck\">.\n"
             "- Cada <section> es una diapositiva de 1920x1080; el fondo va como clase (fondo, fondo-profundo, fondo-claro, fondo-niebla).\n"
             "- Las diapositivas @pilares, @repaso, @seguimiento y @plataforma de este kit son ejemplos: "
             "cópialas y cambia los textos con los datos de la clase anterior y el pilar de la clase.\n"
             "- Notas del orador en <aside> al final de cada <section>: no se ven en pantalla (tecla P = vista de presentador).\n"
             "- Teclas: flechas o clic para avanzar, F pantalla completa, P presentador.\n-->\n")
    return aviso + html


def main():
    clases = cargar_clases()
    SALIDA.mkdir(exist_ok=True)
    k = CONOCIMIENTO
    archivos = {
        "01-programa.md": unir("Programa BeCoach: marco, estructura y reglas", [
            ("conocimiento/marco-programa.md", leer(k / "marco-programa.md")),
            ("conocimiento/pilares.json", "```json\n" + leer(k / "pilares.json") + "\n```"),
            ("conocimiento/estructura-clase.md", leer(k / "estructura-clase.md")),
            ("conocimiento/reglas-aprendidas.md", leer(k / "reglas-aprendidas.md")),
            ("conocimiento/decisiones.md", leer(k / "decisiones.md")),
        ]),
        "02-diseno.md": unir("Diseño de las presentaciones", [
            ("conocimiento/guia-diseno.md", leer(k / "guia-diseno.md")),
        ]),
        "03-historial.md": unir("Historial del programa: clases, temas, glosario e ideas", [
            ("conocimiento/bitacora.md", leer(k / "bitacora.md")),
            ("conocimiento/mapa-temas.md", leer(k / "mapa-temas.md")),
            ("conocimiento/glosario.md", leer(k / "glosario.md")),
            ("conocimiento/ideas-temas.md", leer(k / "ideas-temas.md")),
        ]),
    }
    carpeta, datos = clases[-1]
    archivos["04-ultima-clase.md"] = unir(f"Última clase: {datos.get('numero', 0):03d} · {datos.get('titulo')}", [
        (f"clases/{carpeta.name}/clase.json", "```json\n" + json.dumps(datos, ensure_ascii=False, indent=2) + "\n```"),
        (f"clases/{carpeta.name}/contenido.md", leer(carpeta / "contenido.md")),
    ])
    archivos["kit-presentacion.html"] = kit(clases)
    archivos["plantillas-diapositivas.html"] = "\n\n".join(
        f"<!-- Plantilla: {p.stem} -->\n{leer(p)}" for p in sorted((PLANTILLAS / "slides").glob("*.html")))
    for nombre, texto in archivos.items():
        (SALIDA / nombre).write_text(texto + "\n", encoding="utf-8")
        print(f"{nombre}: {len(texto.encode('utf-8')) // 1024} KB")


if __name__ == "__main__":
    main()
