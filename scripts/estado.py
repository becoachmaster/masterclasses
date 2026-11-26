"""Resumen del estado del programa. El hook SessionStart lo inyecta al inicio de cada sesión."""
from _comun import SIGUIENTE_PASO, cargar_clases, nombre_pilar, pilares


def main():
    try:
        clases = cargar_clases()
    except ValueError as e:
        print(f"⚠ {e}")
        return
    ps = pilares()
    print("## Estado del programa BeCoach (automático)")
    print("Pilares: " + " · ".join(p["nombre"] + (" (provisional)" if p.get("provisional") else "") for p in ps))
    if not clases:
        print("Aún no hay clases. Empieza con /nueva-clase <idea central>.")
        return
    print(f"Clases registradas: {len(clases)}")
    for _, d in clases[-3:]:
        print(f"- {d.get('numero', 0):03d} · {d.get('titulo')} · {nombre_pilar(d.get('pilar'))} · estado: {d.get('estado')} · fecha: {d.get('fecha') or 'por definir'}")
    abiertas = [c for c in clases if c[1].get("estado") != "cerrada"]
    if abiertas:
        carpeta, d = abiertas[-1]
        print(f"Clase en curso: {d.get('numero', 0):03d} ({carpeta.name}) · siguiente paso: {SIGUIENTE_PASO.get(d.get('estado'), 'revisar clase.json')}")
        print("Artefacto de la presentación: " + (d.get("artefacto") or "aún no publicado (se publica en la Fase 4)"))
        faltan = [c for c in ("aprendizajes", "frase_ancla", "compromiso", "bucle_abierto") if not d.get(c)]
        if faltan:
            print("Campos pendientes para poder cerrarla: " + ", ".join(faltan))
    conteo = {p["id"]: 0 for p in ps}
    for _, d in clases:
        if d.get("pilar") in conteo:
            conteo[d["pilar"]] += 1
    menor = min(conteo.values())
    print("Pilar menos trabajado: " + ", ".join(nombre_pilar(k) for k, v in conteo.items() if v == menor))
    ultima = clases[-1][1]
    if ultima.get("bucle_abierto"):
        print(f"Bucle abierto pendiente: {ultima['bucle_abierto']}")
    print("Recuerda: sigue CLAUDE.md, registra correcciones en conocimiento/reglas-aprendidas.md y decisiones en conocimiento/decisiones.md.")


if __name__ == "__main__":
    main()
