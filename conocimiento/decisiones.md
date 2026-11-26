# Decisiones del programa

Registro con fecha. Claude agrega una entrada cada vez que Gio decide algo sobre el programa.

- 2026-09-24 · Formato: clase en vivo por Zoom de 50 minutos, un ejercicio individual de auto-observación, sin salas de grupos.
- 2026-09-29 · Cada clase abre con los 3 pilares del liderazgo personal y con los aprendizajes de la clase anterior.
- 2026-09-29 · El nombre del tercer pilar ("Sostenimiento") es provisional.
- 2026-09-30 · Las clases son abiertas. El objetivo actual es construir comunidad. El programa pago se lanzará cuando Gio se sienta listo.
- 2026-09-30 · El sistema de clases vive en Claude Code para actualizar la base de conocimiento de forma automática y conectarse con los próximos proyectos.
- 2026-09-30 · Próximo proyecto: sitio web donde se alojarán las clases (presentación y notas públicas de cada una).
- 2026-09-29 · El tercer pilar pasa a llamarse "Integración" (antes "Sostenimiento", provisional). El id `sostenimiento` se mantiene.
- 2026-09-29 · Color de acento vibrante: Brasa `#FF5A1F` (segunda opción considerada: Lima). Una sola aparición por diapositiva; el café pasa a color de apoyo.
- 2026-09-29 · Descripción definitiva del pilar Integración: "Llevar lo declarado a la práctica diaria y sostenerlo en el tiempo." (brief de la clase 002).
- 2026-09-29 · Clase 002 · Identidad de equipo, pilar Conexión, jueves 2026-10-01. Brief en `entradas/brief-002-identidad.md`.
- 2026-09-30 · La propuesta de bucle abierto de la clase 001 hacia el pilar de Conexión es de Claude. Gio puede cambiarla.
- 2026-10-27 · Desde la clase 003, la cámara se graba aparte con OBS y el video que se publica es un montaje de diapositivas (Zoom) y cámara, con la misma línea de tiempo de Zoom. Editor y planes en `C:\Dev\becoach-platform\tools\montaje\`.
- 2026-11-02 · Nuevo sistema visual de las diapositivas: cristal, fondos con degradado y brillos Brasa, el mismo de los gráficos de video y los reels. Aprobado por Gio en la hoja de estilo de Claude Design. Se aplica desde la clase 5; las clases 001-004 conservan su estilo. Muestra en `plantillas/muestra/`.

## 2026-11-05 · Estructura flexible de las clases
- Las clases estaban saliendo iguales (mismas preguntas, títulos y elementos) y el material fuente se recortaba. Gio pidió una estructura más flexible.
- Solo el ritual de apertura y cierre es fijo. El centro se diseña con un arco elegido según el material (problema → modelo → herramienta, mito → evidencia, caso → disección, mapa → zoom, dos observadores, pregunta abierta, serie), con bancos de movimientos e interacciones y reglas contra la repetición.
- El material fuente se guarda completo en `clases/NNN/fuente/` y se inventaría con el destino de cada elemento.
- Se traen las plantillas de datos del sistema original de slides al de cristal: `barras`, `dona`, `tabla`, `pendiente`, `cuadrante`.

## 2026-11-26 · Presentaciones como artefactos de Claude
- Gio decidió llevar el proyecto a Claude: las presentaciones se publican como artefactos privados en claude.ai y, más adelante, la carpeta pasa a un proyecto en la nube (claude.ai/code) con `/send-to-project`.
- Se publica la presentación tal cual, con el motor de cristal (opción elegida frente al tipo «Slides» nativo, para no perder `@pilares`, `@repaso`, notas del orador ni el estilo).
- El link de cada clase se guarda en el campo `artefacto` de `clase.json` y se republica en cada ajuste. El hook avisa cuándo republicar. Primera clase publicada: la 006.
- El archivo local `presentacion.html` sigue siendo la fuente y el respaldo para proyectar en Zoom.
