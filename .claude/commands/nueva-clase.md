---
description: Inicia una clase nueva a partir de la idea central y del material fuente de Gio (Fases 0, 1 y 2). Úsalo siempre que Gio traiga un tema, un documento, un taller o notas para una clase nueva.
argument-hint: <idea central de la clase, o ruta del material fuente>
---
Idea central o material: $ARGUMENTS

## Por qué este flujo es así
Las clases empezaron a salir todas iguales y el material de Gio se recortaba para caber en una estructura fija. Ahora el material manda: primero se inventaría todo lo que trae, después se elige la forma de la clase que mejor lo sirve. Gio aprueba cada fase.

## 0 · Arranque
1. El estado del programa llega al iniciar la sesión (si no, `python scripts/estado.py`). Lee `conocimiento/mapa-temas.md`, `conocimiento/ideas-temas.md` y el `clase.json` de la última clase.
2. Si la última clase no está `cerrada`, ciérrala primero con `.claude/commands/cerrar-clase.md`. Pregúntale a Gio en un solo mensaje lo que no puedas saber; si no responde, ciérrala con lo que hay.
3. Crea la carpeta: `python scripts/nueva_clase.py "<título provisional>" --idea "<idea central>"`.
4. Guarda el material fuente completo, sin resumir, en `clases/NNN-slug/fuente/` (copia los archivos o pega el texto en `fuente/material.md`). Las imágenes y gráficos que traiga van ahí también.

## 0.5 · Inventario de la fuente
Lee el material completo y escribe `fuente/inventario.md`: una tabla con **cada** elemento que trae (concepto, distinción, dato o cifra, gráfico o tabla, ejemplo, cita, ejercicio, frase, historia) y su destino:

| Elemento | Tipo | Destino |
|---|---|---|
| … | dato | pantalla · notas del orador · guía descargable · banco de ideas · próxima clase |

No hay destino "descartado" sin que Gio lo apruebe. Si algo no cabe en 50 minutos, va a las notas, a la guía o a una clase futura (`ideas-temas.md`), pero no se pierde. Los datos y gráficos del material se conservan con su fuente y, si sirven a la pregunta guía, se muestran con las plantillas de datos (`cifra`, `barras`, `dona`, `tabla`, `pendiente`, `cuadrante`).

## 1 · Enfoque ✋
Presenta en pocas líneas:
- Tesis en una frase y transformación (de X a Y).
- Pilar (id de `conocimiento/pilares.json`). Si encaja mejor en otro o repite algo ya visto, dilo.
- **Arco** elegido de `conocimiento/estructura-clase.md` (sección 3) y por qué le sirve a este material. Distinto del arco de la clase anterior.
- Quiebre de apertura, con un formato distinto al de las dos clases anteriores.
- Conexión con la clase anterior (cómo responde a su bucle abierto) y bucle abierto para la siguiente.
- Dos o tres títulos posibles.
- Resumen del inventario: cuántos elementos trae el material y adónde va cada grupo.

Espera la aprobación de Gio. Guarda en `clase.json` y pasa el estado a `temario`.

## 2 · Temario ✋
Los bloques del centro según el arco, cada uno nombrado por lo que trata, con: qué pregunta del participante responde, qué elementos del inventario usa, qué movimientos y qué interacción lleva (de los bancos de `estructura-clase.md`), y qué datos o gráficos se muestran. Revisa la sección 7 (contra la repetición) antes de presentarlo.

Luego sigue con la Fase 3 (escaleta) según `CLAUDE.md`, con aprobación de Gio.
