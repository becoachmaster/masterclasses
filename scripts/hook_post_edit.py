"""Hook PostToolUse: mantiene la base de conocimiento y las presentaciones al día sin intervención.

- Cambió un clase.json o pilares.json → regenera índices y reconstruye las presentaciones afectadas.
- Cambió una diapositiva o un deck.json → reconstruye la presentación de esa clase y revisa el estilo.
Si hay advertencias, sale con código 2 para que Claude las vea y las corrija.
"""
import json
import subprocess
import sys
from pathlib import Path

from _comun import CLASES, CONOCIMIENTO, RAIZ, cargar_clases

SCRIPTS = Path(__file__).resolve().parent


def correr(*args):
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True, cwd=RAIZ)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    try:
        evento = json.load(sys.stdin)
    except Exception:
        return 0
    entrada = evento.get("tool_input") or {}
    ruta = entrada.get("file_path") or entrada.get("path") or ""
    if not ruta:
        return 0
    ruta = Path(ruta)
    if not ruta.is_absolute():
        ruta = (RAIZ / ruta)
    ruta = ruta.resolve()

    avisos = []
    try:
        relativa = ruta.relative_to(CLASES.resolve())
        carpeta_clase = CLASES / relativa.parts[0]
    except (ValueError, IndexError):
        carpeta_clase = None

    es_pilares = ruta == (CONOCIMIENTO / "pilares.json").resolve()
    es_ficha = carpeta_clase is not None and ruta.name == "clase.json"
    es_slide = carpeta_clase is not None and "slides" in ruta.parts

    if not (es_pilares or es_ficha or es_slide):
        return 0

    if es_pilares or es_ficha:
        codigo, salida = correr(str(SCRIPTS / "actualizar_indices.py"))
        if codigo == 2:
            avisos.append(salida.strip())

    objetivos = []
    if es_pilares:
        objetivos = ["--todas"]
    elif es_slide:
        objetivos = [carpeta_clase.name]
    elif es_ficha:
        objetivos = [carpeta_clase.name]
        try:
            numeros = [d.get("numero") for c, d in cargar_clases()]
            actual = next(d.get("numero") for c, d in cargar_clases() if c.name == carpeta_clase.name)
            siguientes = [n for n in numeros if n and n > actual]
            if siguientes:
                objetivos.append(str(min(siguientes)))
        except Exception:
            pass

    antes = huellas()
    for obj in objetivos:
        codigo, salida = correr(str(SCRIPTS / "construir_presentacion.py"), obj)
        if codigo == 2:
            avisos.append(salida.strip())
        correr(str(SCRIPTS / "exportar_contenido.py"), obj)
    republicar = artefactos_desactualizados(antes)

    if avisos:
        print("Revisión automática del proyecto BeCoach:\n" + "\n".join(avisos + republicar), file=sys.stderr)
        return 2
    if republicar:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "\n".join(republicar)}}, ensure_ascii=False))
    return 0


def huellas():
    """Fecha de modificación de cada presentacion.html, para saber cuáles cambió la reconstrucción."""
    return {c.name: (c / "presentacion.html").stat().st_mtime_ns
            for c, _ in cargar_clases() if (c / "presentacion.html").exists()}


def artefactos_desactualizados(antes):
    """Clases con artefacto publicado cuya presentacion.html acaba de cambiar: hay que republicarlas."""
    despues = huellas()
    mensajes = []
    for carpeta, datos in cargar_clases():
        url = datos.get("artefacto")
        if url and despues.get(carpeta.name) != antes.get(carpeta.name):
            mensajes.append(
                f"La presentación de la clase {datos.get('numero', 0):03d} cambió y su artefacto ({url}) quedó "
                f"desactualizado. Cuando termines los cambios de este turno, republícala con la herramienta Artifact "
                f"(url={url}, file_path=clases/{carpeta.name}/presentacion.html; ver CLAUDE.md, «Presentaciones como artefactos»).")
    return mensajes


if __name__ == "__main__":
    sys.exit(main())
