"""Exporta el contenido de una clase a clases/NNN-slug/contenido.md: ficha, diapositivas en orden y notas del orador.

Uso: python scripts/exportar_contenido.py [clase] [--todas]
El archivo se genera a partir de clase.json y slides/. No lo edites a mano.
"""
import argparse
import re
import sys
from html.parser import HTMLParser

from _comun import RAIZ, buscar_clase, cargar_clases, clase_anterior, escribir_si_cambia, leer_json, nombre_pilar, pilares

BLOQUES = {"h1", "h2", "h3", "p"}
OMITIR = {"BeCoach · Arquitectura del Ser"}


def limpiar(texto):
    return re.sub(r"\s+", " ", texto.replace("\xa0", " ")).strip()


class Lector(HTMLParser):
    """Recorre una diapositiva y separa lo visible (en orden) de las notas del orador."""

    def __init__(self):
        super().__init__()
        self.items, self.notas = [], []
        self.pila, self.buffer, self.fila = [], [], None
        self.en_aside = self.en_svg_texto = False
        self.svg_textos = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "aside":
            self.en_aside = True
        elif tag == "br":
            self.buffer.append(" ")
        elif tag == "svg":
            self.svg_textos = []
            if a.get("aria-label"):
                self.items.append(("ilustracion", a["aria-label"]))
        elif tag == "text":
            self.en_svg_texto = True
            self.buffer = []
        elif tag == "img":
            self.items.append(("imagen", (a.get("alt", ""), a.get("src", ""))))
        elif tag == "video":
            self.items.append(("video", a.get("src", "")))
        elif tag == "tr":
            self.fila = []
        elif tag in BLOQUES | {"td", "th"}:
            self.pila.append(tag)
            self.buffer = []

    def handle_endtag(self, tag):
        if tag == "aside":
            self.en_aside = False
        elif tag == "text":
            self.en_svg_texto = False
            self.svg_textos.append(limpiar("".join(self.buffer)))
        elif tag == "svg" and self.svg_textos:
            self.items.append(("etiquetas", " · ".join(t for t in self.svg_textos if t)))
            self.svg_textos = []
        elif tag == "tr" and self.fila is not None:
            self.items.append(("fila", " | ".join(self.fila)))
            self.fila = None
        elif self.pila and tag == self.pila[-1]:
            self.pila.pop()
            texto = limpiar("".join(self.buffer))
            if not texto or texto in OMITIR:
                return
            if tag in ("td", "th") and self.fila is not None:
                self.fila.append(texto)
            else:
                self.items.append((tag, texto))

    def handle_data(self, data):
        if self.en_aside:
            self.notas.append(data)
        elif self.en_svg_texto or self.pila:
            self.buffer.append(data)


def leer_slide(html):
    lector = Lector()
    lector.feed(html)
    return lector.items, limpiar("".join(lector.notas))


def unir_marcadores(items):
    """Une las letras o números sueltos (A, B, 1, 2) con el texto que les sigue: 'A · Yo solo'."""
    unidos, prefijo = [], None
    for tipo, valor in items:
        if tipo == "p" and isinstance(valor, str) and len(valor) <= 2:
            prefijo = valor
            continue
        if prefijo and isinstance(valor, str):
            valor = f"{prefijo} · {valor}"
        prefijo = None
        unidos.append((tipo, valor))
    return unidos


def md_slide(n, items, notas):
    items = unir_marcadores(items)
    # Sin h1/h2 (fotos, video, ejercicios), el título es el primer texto de la diapositiva.
    titulo = next((t for tipo, t in items if tipo in ("h1", "h2")), None) or next((t for tipo, t in items if tipo == "p"), "Diapositiva")
    lineas = [f"### {n}. {titulo}", ""]
    for tipo, valor in items:
        if tipo in ("h1", "h2", "p") and valor == titulo:
            continue
        if tipo == "h3":
            lineas.append(f"- **{valor}**")
        elif tipo in ("h1", "h2", "p"):
            lineas.append(f"- {valor}")
        elif tipo == "fila":
            lineas.append(f"- {valor}")
        elif tipo == "etiquetas":
            lineas.append(f"- {valor}")
        elif tipo == "ilustracion":
            lineas.append(f"- *Ilustración: {valor}*")
        elif tipo == "imagen":
            alt, src = valor
            lineas.append(f"- ![{alt}]({src})")
        elif tipo == "video":
            lineas.append(f"- Video: [{src_nombre(valor)}]({valor})")
    if notas:
        if len(lineas) > 2:
            lineas.append("")
        lineas.append(f"> **Notas del orador:** {notas}")
    return lineas + [""]


def src_nombre(src):
    return src.rsplit("/", 1)[-1]


def md_automatica(id_slide, datos, previa, n):
    if id_slide.startswith("@plataforma"):
        return [f"### {n}. app.becoach.pro", "", "- Todas las clases", "- Guías prácticas", "- Descargables", "- Acceso gratuito", ""]
    if id_slide == "@pilares":
        filas = [f"- **{p['nombre']}**{' (pilar de hoy)' if p['id'] == datos.get('pilar') else ''}: {p['descripcion']}" for p in pilares()]
        return [f"### {n}. Los 3 pilares del liderazgo personal", "", *filas, ""]
    if previa is None:
        return []
    ant = previa[1]
    if id_slide == "@repaso":
        filas = [f"{i}. {a}" for i, a in enumerate(ant.get("aprendizajes", []), 1)]
        return [f"### {n}. Lo que aprendimos la clase anterior", "", f"*{ant.get('titulo', '')}*", "", *filas, "", f"> “{ant.get('frase_ancla', '')}”", ""]
    if id_slide == "@seguimiento":
        return [f"### {n}. ¿Cumpliste tu compromiso?", "", f"- {ant.get('compromiso', '')}", ""]
    return []


def exportar(carpeta, datos):
    deck = leer_json(carpeta / "slides" / "deck.json")
    previa = clase_anterior(datos.get("numero", 0))
    tr = datos.get("transformacion") or {}
    salida = [
        f"# {datos.get('titulo', '')}",
        "",
        "> Archivo generado por `scripts/exportar_contenido.py` a partir de `clase.json` y `slides/`. No lo edites a mano.",
        "",
        f"- **Clase:** {datos.get('numero', 0):03d}",
        f"- **Fecha:** {datos.get('fecha') or 'por definir'}",
        f"- **Pilar:** {nombre_pilar(datos.get('pilar'))}",
        f"- **Estado:** {datos.get('estado', '')}",
        "",
        "## Ficha",
        "",
        f"- **Tesis:** {datos.get('tesis', '')}",
        f"- **Transformación:** de {tr.get('de', '')} a {tr.get('a', '')}.",
        f"- **Quiebre:** {datos.get('quiebre', '')}",
        f"- **Ejercicio:** {datos.get('ejercicio', '')}",
        f"- **Compromiso:** {datos.get('compromiso', '')}",
        f"- **Bucle abierto:** {datos.get('bucle_abierto', '')}",
        f"- **Frase ancla:** {datos.get('frase_ancla', '')}",
        "",
    ]
    if datos.get("temas"):
        salida += ["**Temas:** " + " · ".join(datos["temas"]), ""]
    if datos.get("herramientas"):
        salida += ["**Herramientas:** " + " · ".join(datos["herramientas"]), ""]
    if datos.get("terminos"):
        salida += ["### Distinciones", "", "| Término | Definición |", "|---|---|"]
        salida += [f"| {t['termino']} | {t['definicion']} |" for t in datos["terminos"]] + [""]
    if datos.get("fuentes"):
        salida += ["### Fuentes", ""] + [f"- {f}" for f in datos["fuentes"]] + [""]

    salida += ["## Diapositivas", ""]
    for n, id_slide in enumerate(deck.get("orden", []), 1):
        if id_slide.startswith("@"):
            salida += md_automatica(id_slide, datos, previa, n)
            continue
        archivo = carpeta / "slides" / f"{id_slide}.html"
        if not archivo.exists():
            continue
        items, notas = leer_slide(archivo.read_text(encoding="utf-8"))
        divisor = next((t for tipo, t in items if tipo == "p" and re.fullmatch(r"P\.\d+", t)), None)
        if divisor:
            titulo = next((t for tipo, t in items if tipo == "h2"), "")
            salida += [f"## {divisor} · {titulo}", ""] + ([f"> **Notas del orador:** {notas}", ""] if notas else [])
            continue
        salida += md_slide(n, items, notas)

    destino = carpeta / "contenido.md"
    escribir_si_cambia(destino, "\n".join(salida).rstrip() + "\n")
    return destino


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("clase", nargs="?")
    ap.add_argument("--todas", action="store_true")
    a = ap.parse_args()
    objetivos = cargar_clases() if a.todas else [buscar_clase(a.clase)]
    if not objetivos or objetivos[0] is None:
        sys.exit("No encontré la clase.")
    for carpeta, datos in objetivos:
        if (carpeta / "slides" / "deck.json").exists():
            print(exportar(carpeta, datos).relative_to(RAIZ))


if __name__ == "__main__":
    main()
