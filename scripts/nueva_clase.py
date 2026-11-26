"""Crea la carpeta de una clase nueva con su clase.json, escaleta y diapositivas base.

Uso: python scripts/nueva_clase.py "Título provisional" --idea "Idea central" [--fecha AAAA-MM-DD] [--pilar id]
"""
import argparse
import datetime
import subprocess
import sys
from pathlib import Path

from _comun import CLASES, PLANTILLAS, cargar_clases, escribir_json, esc, leer_json, slugify


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("titulo")
    ap.add_argument("--idea", default="")
    ap.add_argument("--fecha", default=None)
    ap.add_argument("--pilar", default=None)
    a = ap.parse_args()

    clases = cargar_clases()
    numero = (clases[-1][1].get("numero", 0) + 1) if clases else 1
    slug = slugify(a.titulo)
    carpeta = CLASES / f"{numero:03d}-{slug}"
    if carpeta.exists():
        sys.exit(f"Ya existe {carpeta}")
    (carpeta / "slides").mkdir(parents=True)
    (carpeta / "recursos").mkdir()

    datos = leer_json(PLANTILLAS / "clase.json")
    hoy = datetime.date.today().isoformat()
    datos.update({
        "numero": numero,
        "slug": slug,
        "titulo": a.titulo,
        "fecha": a.fecha,
        "estado": "enfoque",
        "pilar": a.pilar,
        "idea_central": a.idea,
        "conexion_anterior": clases[-1][1].get("numero") if clases else None,
        "historial": [{"fecha": hoy, "evento": "Clase creada"}],
    })
    escribir_json(carpeta / "clase.json", datos)

    escaleta = (PLANTILLAS / "escaleta.md").read_text(encoding="utf-8")
    (carpeta / "escaleta.md").write_text(escaleta.replace("{{TITULO}}", a.titulo), encoding="utf-8")

    portada = (PLANTILLAS / "slides" / "portada.html").read_text(encoding="utf-8")
    (carpeta / "slides" / "portada.html").write_text(portada.replace("{{TITULO}}", esc(a.titulo)), encoding="utf-8")

    orden = ["portada", "@pilares"]
    if clases:
        orden += ["@repaso", "@seguimiento"]
    orden += ["@plataforma"]  # las diapositivas de la clase van antes; la frase ancla, después
    escribir_json(carpeta / "slides" / "deck.json", {"titulo": a.titulo, "estilo": "cristal", "orden": orden})

    aqui = Path(__file__).resolve().parent
    subprocess.run([sys.executable, str(aqui / "actualizar_indices.py")], check=False)
    subprocess.run([sys.executable, str(aqui / "construir_presentacion.py"), str(numero)], check=False)
    print(f"Clase {numero:03d} creada en {carpeta}")


if __name__ == "__main__":
    main()
