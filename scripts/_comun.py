"""Utilidades compartidas por los scripts del proyecto. Solo librería estándar."""
import json
import re
import sys
import unicodedata
from pathlib import Path

# Windows usa cp1252 por defecto: fuerza UTF-8 para que tildes y ñ salgan bien.
for _flujo in (sys.stdout, sys.stderr):
    if hasattr(_flujo, "reconfigure"):
        _flujo.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
CLASES = RAIZ / "clases"
CONOCIMIENTO = RAIZ / "conocimiento"
MOTOR = RAIZ / "motor"
PLANTILLAS = RAIZ / "plantillas"

ESTADOS = ["idea", "enfoque", "temario", "escaleta", "presentacion", "dictada", "cerrada"]
SIGUIENTE_PASO = {
    "idea": "Definir el enfoque (Fase 1) y pedir aprobación a Gio.",
    "enfoque": "Presentar o ajustar el enfoque (Fase 1) y esperar la aprobación de Gio.",
    "temario": "Construir el temario (Fase 2) y esperar la aprobación de Gio.",
    "escaleta": "Escribir la escaleta minuto a minuto (Fase 3) y esperar la aprobación de Gio.",
    "presentacion": "Construir o ajustar las diapositivas (Fase 4-5) con /presentacion.",
    "dictada": "Cerrar la clase con /cerrar-clase (aprendizajes, notas públicas, bitácora).",
    "cerrada": "Nada pendiente. Siguiente clase con /nueva-clase <idea>.",
}


def slugify(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t[:60].strip("-") or "clase"


def leer_json(ruta):
    return json.loads(Path(ruta).read_text(encoding="utf-8"))


def escribir_json(ruta, datos):
    Path(ruta).write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def escribir_si_cambia(ruta, texto):
    ruta = Path(ruta)
    if ruta.exists() and ruta.read_text(encoding="utf-8") == texto:
        return False
    ruta.write_text(texto, encoding="utf-8")
    return True


def cargar_clases():
    """Devuelve [(carpeta, datos)] ordenado por número. Lanza ValueError si un clase.json está mal formado."""
    resultado = []
    if not CLASES.exists():
        return resultado
    for carpeta in CLASES.iterdir():
        archivo = carpeta / "clase.json"
        if carpeta.is_dir() and archivo.exists():
            try:
                datos = leer_json(archivo)
            except json.JSONDecodeError as e:
                raise ValueError(f"{archivo.relative_to(RAIZ)} no es JSON válido: {e}")
            resultado.append((carpeta, datos))
    return sorted(resultado, key=lambda par: par[1].get("numero", 0))


def pilares():
    return leer_json(CONOCIMIENTO / "pilares.json")["pilares"]


def nombre_pilar(pid):
    for p in pilares():
        if p["id"] == pid:
            return p["nombre"]
    return pid or "Sin pilar"


def buscar_clase(ref=None):
    """Acepta número ('2', '002'), slug, nombre de carpeta o ruta. Sin ref: la última clase no cerrada, o la última."""
    clases = cargar_clases()
    if not clases:
        return None
    if ref is None:
        abiertas = [c for c in clases if c[1].get("estado") != "cerrada"]
        return (abiertas or clases)[-1]
    ref = str(ref).strip().rstrip("/")
    ruta = Path(ref)
    for carpeta, datos in clases:
        if ref.isdigit() and int(ref) == datos.get("numero"):
            return carpeta, datos
        if ref in (carpeta.name, datos.get("slug")) or ruta.resolve() == carpeta.resolve():
            return carpeta, datos
    return None


def clase_anterior(numero):
    previas = [c for c in cargar_clases() if c[1].get("numero", 0) < numero]
    return previas[-1] if previas else None


def esc(texto):
    return (str(texto).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))
