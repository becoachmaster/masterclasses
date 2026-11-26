"""Regenera la bitácora, el mapa de temas y el glosario a partir de todos los clase.json.

Uso: python scripts/actualizar_indices.py
"""
import sys
from collections import OrderedDict

from _comun import CONOCIMIENTO, cargar_clases, escribir_si_cambia, nombre_pilar, pilares

AVISO = "> Archivo generado automáticamente por `scripts/actualizar_indices.py` a partir de `clases/*/clase.json`. No lo edites a mano.\n"


def lista(items):
    return "\n".join(f"- {i}" for i in items) if items else "- (sin registrar)"


def bitacora(clases):
    out = ["# Bitácora de clases", "", AVISO, "| N° | Fecha | Clase | Pilar | Estado |", "|---|---|---|---|---|"]
    for carpeta, d in clases:
        out.append(f"| {d.get('numero', 0):03d} | {d.get('fecha') or 'por definir'} | [{d.get('titulo', '')}](../clases/{carpeta.name}/) | {nombre_pilar(d.get('pilar'))} | {d.get('estado', '')} |")
    for carpeta, d in clases:
        tr = d.get("transformacion") or {}
        out += [
            "", f"## {d.get('numero', 0):03d} · {d.get('titulo', '')}", "",
            f"- **Fecha:** {d.get('fecha') or 'por definir'} · **Pilar:** {nombre_pilar(d.get('pilar'))} · **Estado:** {d.get('estado', '')}",
            f"- **Tesis:** {d.get('tesis') or '(pendiente)'}",
            f"- **Transformación:** de {tr.get('de') or '…'} a {tr.get('a') or '…'}",
            f"- **Quiebre de apertura:** {d.get('quiebre') or '(pendiente)'}",
            f"- **Ejercicio:** {d.get('ejercicio') or '(pendiente)'}",
            f"- **Frase ancla:** {d.get('frase_ancla') or '(pendiente)'}",
            f"- **Compromiso pedido:** {d.get('compromiso') or '(pendiente)'}",
            f"- **Bucle abierto hacia la siguiente clase:** {d.get('bucle_abierto') or '(pendiente)'}",
            "", "**Aprendizajes clave**", lista(d.get("aprendizajes", [])),
            "", "**Temas**", lista(d.get("temas", [])),
            "", "**Herramientas**", lista(d.get("herramientas", [])),
        ]
        if d.get("observaciones_post_clase"):
            out += ["", f"**Cómo fue la clase:** {d['observaciones_post_clase']}"]
    return "\n".join(out) + "\n"


def mapa(clases):
    out = ["# Mapa de temas", "", AVISO, "## Cobertura por pilar", "", "| Pilar | Clases | Títulos |", "|---|---|---|"]
    conteo = {}
    for p in pilares():
        propias = [d for _, d in clases if d.get("pilar") == p["id"]]
        conteo[p["id"]] = len(propias)
        nombre = p["nombre"] + (" (nombre provisional)" if p.get("provisional") else "")
        out.append(f"| {nombre} | {len(propias)} | {'; '.join(d.get('titulo', '') for d in propias) or '—'} |")
    sin_pilar = [d for _, d in clases if not d.get("pilar")]
    if sin_pilar:
        out.append(f"| Sin pilar asignado | {len(sin_pilar)} | {'; '.join(d.get('titulo', '') for d in sin_pilar)} |")
    if conteo:
        menor = min(conteo.values())
        menos = [nombre_pilar(k) for k, v in conteo.items() if v == menor]
        out += ["", f"**Pilar menos trabajado:** {', '.join(menos)} ({menor} clases)."]

    def indice(campo):
        idx = OrderedDict()
        for _, d in clases:
            for t in d.get(campo, []):
                idx.setdefault(t.strip(), []).append(f"{d.get('numero', 0):03d}")
        return idx

    out += ["", "## Temas tocados", ""]
    temas = indice("temas")
    out += [f"- {t} · clases {', '.join(n)}" for t, n in sorted(temas.items(), key=lambda x: x[0].lower())] or ["- (ninguno aún)"]
    out += ["", "## Herramientas y ejercicios", ""]
    herr = indice("herramientas")
    out += [f"- {t} · clases {', '.join(n)}" for t, n in herr.items()] or ["- (ninguna aún)"]
    out += ["", "## Secuencia del programa", ""]
    for _, d in clases:
        out.append(f"{d.get('numero', 0):03d}. {d.get('titulo', '')} → bucle abierto: {d.get('bucle_abierto') or '(pendiente)'}")
    if clases:
        ultima = clases[-1][1]
        out += ["", "## Hilo pendiente", "", f"La próxima clase debería responder: **{ultima.get('bucle_abierto') or '(la última clase aún no tiene bucle abierto)'}**"]
    return "\n".join(out) + "\n"


def glosario(clases):
    terminos = OrderedDict()
    for _, d in clases:
        for t in d.get("terminos", []):
            clave = t.get("termino", "").strip()
            if clave and clave.lower() not in {k.lower() for k in terminos}:
                terminos[clave] = (t.get("definicion", ""), d.get("numero", 0), d.get("titulo", ""))
    out = ["# Glosario ontológico del programa", "", AVISO, "Lenguaje común que se construye clase a clase.", ""]
    for termino in sorted(terminos, key=str.lower):
        definicion, num, titulo = terminos[termino]
        out.append(f"- **{termino}:** {definicion} *(clase {num:03d}: {titulo})*")
    if not terminos:
        out.append("- (sin términos aún)")
    return "\n".join(out) + "\n"


def main():
    try:
        clases = cargar_clases()
    except ValueError as e:
        print(f"⚠ {e}", file=sys.stderr)
        sys.exit(2)
    cambios = []
    for nombre, contenido in (("bitacora.md", bitacora(clases)), ("mapa-temas.md", mapa(clases)), ("glosario.md", glosario(clases))):
        if escribir_si_cambia(CONOCIMIENTO / nombre, contenido):
            cambios.append(nombre)
    print("Índices actualizados: " + (", ".join(cambios) if cambios else "sin cambios"))


if __name__ == "__main__":
    main()
