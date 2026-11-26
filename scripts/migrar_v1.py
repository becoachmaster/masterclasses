#!/usr/bin/env python3
"""Traduce colores de la marca v1 (tierra y café) a la v2 (azul) en archivos de texto.

Es la tabla de manual/migracion.md ampliada con los tonos intermedios y los rgba que aparecen en el código.
La Brasa no cambia. Los degradados Brasa de tres tonos pasan a dos (brasa alta → brasa).
Sirve para plantillas, estilos y scripts con colores escritos a mano. No toca bloques de marca.

Uso:
  python scripts/migrar_v1.py ARCHIVO_O_CARPETA [...] [--revisar]
  (en carpetas recorre .html .css .js .mjs .py .md .json)

También se importa: from migrar_v1 import a_v2
"""
import argparse
import re
import sys
from pathlib import Path

HEX = {
    "#C9AC91": "#A9BEE0",  # tostado → azul hielo
    "#7A5C4A": "#3D5A8C",  # café → azul acero
    "#3E4A4F": "#3A5A9A",  # mineral → azul luz
    "#1A1918": "#141B2D",  # tinta
    "#5E554D": "#4E5A70",  # piedra → tinta suave
    "#786F66": "#4E5A70",  # muted → tinta suave
    "#F7F5F1": "#F5F7FA",  # papel → nube
    "#F2EEE8": "#F5F7FA",
    "#F2EDE6": "#F5F7FA",  # arena (inicio) → nube
    "#ECE7E0": "#E8EDF4",  # arena → nube baja
    "#E2D9CD": "#E8EDF4",
    "#F1EDE6": "#E8EDF4",
    "#EEF1F2": "#EEF3FA",  # niebla (inicio)
    "#E6EAEC": "#E8EDF4",
    "#D9DFE2": "#D6DFEC",  # niebla (final)
    "#CDD3D6": "#D6DFEC",
    "#D6CEC3": "#D7DEE8",  # borde → línea
    "#E4DED5": "#D7DEE8",
    "#ECE8E1": "#D7DEE8",
    "#B9B1A7": "#A9B4C8",  # humo → gris hielo
    "#2A2725": "#1E2A4E",  # grafito → azul
    "#1E1C1B": "#1E2A4E",  # carbón alto → azul
    "#151413": "#121A33",  # carbón → azul bajo
    "#1C1A19": "#16203B",  # cristal opaco
    "#1F1E1C": "#1A2442",
    "#20292C": "#121A33",  # fondo mineral → fondo profundo
    "#161A1B": "#0A0F1F",
    "#0E0D0C": "#0A0F1F",  # noche → azul noche
    "#FF6B33": "#FF7A45",  # botón viejo → brasa alta
    "#E8480F": "#FF5A1F",
    "#3F7D5C": "#1E7A4C",  # éxito
    "#56788A": "#3D5A8C",  # info → azul acero
    "#B83A3A": "#B3261E",  # error
}

RGB = {
    (247, 245, 241): (245, 247, 250),
    (242, 238, 232): (245, 247, 250),
    (201, 172, 145): (169, 190, 224),
    (122, 92, 74): (61, 90, 140),
    (62, 74, 79): (58, 90, 154),
    (21, 20, 19): (18, 26, 51),
    (26, 25, 24): (20, 27, 45),
    (30, 28, 27): (30, 42, 78),
    (40, 38, 36): (30, 42, 78),
    (20, 19, 18): (18, 26, 51),
    (14, 13, 12): (10, 15, 31),
    (8, 8, 8): (5, 8, 18),
    (74, 52, 38): (30, 42, 78),
    (94, 85, 77): (78, 90, 112),
    (185, 177, 167): (169, 180, 200),
}

_HEX_RE = re.compile("|".join(re.escape(k) for k in HEX), re.I)
_RGB_RE = re.compile(r"rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})")
# Degradado Brasa de tres tonos (…#FF5A1F 55%, #E04A12 100%) → dos tonos (…#FF5A1F 100%)
_BRASA3_RE = re.compile(r"(#FF5A1F)\s*\d+%\s*,\s*#E04A12(\s*100%)?", re.I)
_BLOQUE_RE = re.compile(r"(/\* marca:inicio.*?marca:fin \*/|<!-- marca:inicio.*?marca:fin -->)", re.S)


def _trad(texto):
    n = 0

    def h(m):
        nonlocal n
        n += 1
        return HEX[m.group(0).upper()]

    def r(m):
        nonlocal n
        t = tuple(int(x) for x in m.groups())
        if t not in RGB:
            return m.group(0)
        n += 1
        pre = m.group(0)[: m.group(0).index("(") + 1]
        sep = ", " if ", " in m.group(0) else ","
        return pre + sep.join(str(x) for x in RGB[t])

    def b(m):
        nonlocal n
        n += 1
        return f"{m.group(1)} 100%"

    texto = _HEX_RE.sub(h, texto)
    texto = _RGB_RE.sub(r, texto)
    texto = _BRASA3_RE.sub(b, texto)
    return texto, n


def a_v2(texto):
    """Devuelve (texto traducido, número de cambios). Respeta los bloques de marca."""
    partes = _BLOQUE_RE.split(texto)
    total = 0
    for i in range(0, len(partes), 2):
        partes[i], n = _trad(partes[i])
        total += n
    return "".join(partes), total


EXT = {".html", ".css", ".js", ".mjs", ".py", ".md", ".json"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rutas", nargs="+")
    ap.add_argument("--revisar", action="store_true")
    a = ap.parse_args()
    archivos = []
    for r in map(Path, a.rutas):
        archivos += [p for p in r.rglob("*") if p.suffix in EXT] if r.is_dir() else [r]
    total = 0
    for p in archivos:
        if p.resolve() == Path(__file__).resolve():
            continue
        t = p.read_bytes().decode("utf-8")  # bytes: conserva los finales de línea del archivo
        nuevo, n = a_v2(t)
        if n:
            total += n
            print(f"  {n:4d}  {p}")
            if not a.revisar:
                p.write_bytes(nuevo.encode("utf-8"))
    print(f"{'Por cambiar' if a.revisar else 'Cambiados'}: {total} colores.")
    sys.exit(0)


if __name__ == "__main__":
    main()
