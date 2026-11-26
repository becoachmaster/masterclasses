# BeCoach · Clases semanales de liderazgo

> **Marca:** manual BeCoach v2.1 (https://marca.becoach.pro, local `C:/Dev/becoach-marca`). `motor/deck.css` recibe tokens y clases del manual en su bloque de marca (no lo edites). Las clases 001-006 llevan `"marca": "v1"` en `deck.json` y se construyen con `motor/deck-v1.css` (tierra y café, congelado); las clases nuevas salen en azul con el estilo simple (`"estilo": "simple"`, `motor/simple.css` sobre `deck.css`). `construir_presentacion.py` traduce a la v2 cualquier color v1 que quede (`scripts/migrar_v1.py`).

Este repositorio es el sistema de trabajo de Gio (coach ontológico, marca BeCoach) para diseñar, construir y registrar sus clases semanales abiertas de coaching ontológico para líderes de equipo.

- Formato: clase en vivo por Zoom, 50 minutos, una vez por semana.
- Objetivo actual: **construir comunidad**. Las clases son abiertas y gratuitas. Más adelante se lanzará un programa pago, cuando Gio decida que está listo. No se vende nada en las clases a menos que Gio lo pida.
- Idioma: responde siempre en español neutro/colombiano con tuteo (tú, tienes, estás). Nunca voseo (vos, tenés, sos).

## Lo que importa es el resultado

El entregable de cada clase es la clase diseñada (`clase.json`, escaleta, notas públicas) y su presentación, guardadas en `clases/NNN-slug/` en GitHub. Los scripts, hooks y comandos de este repositorio son ayudas, no requisitos. Si en la nube, o en otro entorno, otro camino llega antes o mejor a ese resultado, úsalo. Lo que sí se mantiene es el contenido (rigor ontológico, tono, continuidad entre clases) y el estilo visual de BeCoach.

## Mapa del repositorio

| Ruta | Qué contiene | ¿Quién lo edita? |
|---|---|---|
| `conocimiento/marco-programa.md` | Propósito, audiencia, método Comprender → Construir → Emerger, tono | Claude, cuando Gio cambia algo del marco |
| `conocimiento/pilares.json` | Los 3 pilares del liderazgo personal (fuente única de sus nombres) | Claude, con `/renombrar-pilar` |
| `conocimiento/estructura-clase.md` | El ritual fijo (apertura y cierre), los arcos para el centro de la clase y los bancos de movimientos e interacciones | Claude, si Gio cambia la estructura |
| `conocimiento/guia-diseno.md` | Sistema visual de las diapositivas (estilo simple, marca v2) | Claude, si Gio cambia el estilo |
| `conocimiento/guia-diseno-cristal.md` | Sistema de cristal anterior, solo para ajustar las clases 005 y 006 | Rara vez |
| `conocimiento/reglas-aprendidas.md` | Correcciones de Gio que aplican siempre | Claude, automáticamente |
| `conocimiento/decisiones.md` | Decisiones del programa, con fecha | Claude, automáticamente |
| `conocimiento/ideas-temas.md` | Banco de ideas de temas | Claude, automáticamente |
| `conocimiento/bitacora.md` | Registro de todas las clases | **Generado por script. No editar.** |
| `conocimiento/mapa-temas.md` | Temas, herramientas y cobertura por pilar | **Generado por script. No editar.** |
| `conocimiento/glosario.md` | Términos ontológicos introducidos, clase por clase | **Generado por script. No editar.** |
| `clases/NNN-slug/clase.json` | Registro estructurado de cada clase (fuente de verdad) | Claude |
| `clases/NNN-slug/fuente/` | Material fuente de Gio completo, sin resumir, e `inventario.md` con el destino de cada elemento | Claude |
| `clases/NNN-slug/escaleta.md` | Minuto a minuto de la clase | Claude |
| `clases/NNN-slug/slides/` | Una diapositiva por archivo `.html` + `deck.json` con el orden | Claude |
| `clases/NNN-slug/presentacion.html` | Presentación final, autocontenida. Se publica como artefacto en claude.ai; su link queda en el campo `artefacto` de `clase.json` | **Generada por script. No editar.** |
| `clases/NNN-slug/contenido.md` | Todo el contenido de la clase en texto: ficha, diapositivas en orden y notas del orador. Léelo en vez de abrir las diapositivas una por una | **Generado por script. No editar.** |
| `clases/NNN-slug/notas-publicas.md` | Resumen para la comunidad y el futuro sitio web | Claude, al cerrar la clase |
| `motor/` | Motor de presentación (CSS, JS, plantilla HTML) | Solo si Gio pide cambios de funcionamiento |
| `plantillas/` | Plantillas de clase, escaleta, notas y diapositivas: `slides-simple/` (estilo simple, para las clases nuevas), `slides/` (sistema de cristal azul) y `slides-v1/` (marca v1). Catálogos: `catalogo-simple.html` y `catalogo.html` | Rara vez |
| `plantillas/muestra/` | La clase 4 completa en el sistema de cristal: referencia visual para copiar. Se construye con `construir_presentacion.py --muestra` | Solo si cambia el sistema |
| `scripts/` | Automatizaciones en Python (solo librería estándar) | Rara vez |

## Contexto con pocos tokens

Lee por capas y detente cuando tengas lo que necesitas:

1. **Siempre:** este archivo + la salida de `estado.py` (llega sola al iniciar la sesión). Con eso ya sabes clase en curso, fase, pilares y bucle abierto. Si en mitad de la conversación necesitas refrescarlo, corre `python scripts/estado.py` (≈700 caracteres) en vez de releer archivos.
2. **Según la tarea:** solo el archivo de conocimiento que aplica (enfoque → `marco-programa.md` y `mapa-temas.md`; temario → `estructura-clase.md`; diapositivas → `guia-diseno.md` y `reglas-aprendidas.md`; cierre → `clase.json` de la clase).
3. **Para copiar estilo:** 2 o 3 diapositivas de `clases/*/slides/`, nunca todas.
4. **Nunca leas** `presentacion.html` (generado, ~70 KB, bloqueado en permisos) ni `motor/deck.js` salvo que Gio pida cambios del motor. Para ubicar algo usa `grep` antes que abrir archivos completos.
5. No vuelvas a leer un archivo que ya leíste en la sesión si no ha cambiado.

## Automatizaciones (ya funcionan solas)

Los hooks de `.claude/settings.json` hacen esto sin que nadie lo pida:

- **Al iniciar cada sesión** se ejecuta `scripts/estado.py`, que te da el estado del programa: última clase, clase en curso, fase actual y pilar menos trabajado.
- **Cada vez que editas un `clase.json` o `pilares.json`** se regeneran la bitácora, el mapa de temas y el glosario, y se reconstruyen las presentaciones afectadas.
- **Cada vez que editas una diapositiva o un `deck.json`** se reconstruyen `presentacion.html` y `contenido.md`, y se revisan las reglas visuales. Si el hook devuelve advertencias, corrígelas antes de seguir.
- **Si una presentación que ya tiene artefacto cambió**, el hook te avisa cuál republicar. Hazlo al terminar los cambios del turno (ver «Presentaciones como artefactos»).

Por eso nunca edites a mano los archivos marcados como generados: se sobrescriben.

## Flujo de trabajo de cada clase

Cada clase avanza por fases. El campo `estado` de `clase.json` refleja la fase: `enfoque → temario → escaleta → presentacion → dictada → cerrada`. En cada fase marcada con ✋ presenta tu propuesta y **espera la aprobación de Gio** antes de avanzar. Actualiza `clase.json` en cuanto Gio apruebe.

**Fase 0. Arranque** (`/nueva-clase <idea central>`)
1. Revisa el estado del programa, la bitácora, el mapa de temas y la ficha de la clase anterior.
2. Si la clase anterior no está `cerrada`, ciérrala primero siguiendo `/cerrar-clase`. Así la continuidad nunca depende de que Gio se acuerde.
3. Crea la carpeta con `python scripts/nueva_clase.py "<título provisional>" --idea "<idea central>"`.
4. Guarda el material fuente completo en `fuente/` y escribe `fuente/inventario.md`: cada concepto, dato, gráfico, ejemplo y cita con su destino. Nada se descarta sin aprobación de Gio.

**Fase 1. Enfoque ✋**
Propón en pocas líneas: la tesis en una frase, la transformación (de X a Y), el pilar, el arco de la clase (de `estructura-clase.md`, distinto del de la clase anterior), el quiebre de apertura, cómo conecta con la clase anterior y qué bucle abierto deja para la siguiente. Si la idea de Gio encaja mejor en otro pilar o repite algo ya visto, dilo.

**Fase 2. Temario ✋**
Los bloques del centro según el arco elegido, cada uno con su contenido, los elementos del inventario que usa, sus datos o gráficos, su interacción, las distinciones ontológicas y el ejercicio de práctica. Solo el ritual de apertura y cierre es fijo; el resto se diseña desde el material.

**Fase 3. Escaleta ✋**
El minuto a minuto en `escaleta.md`: qué se dice, las interacciones de Zoom (chat, encuestas) y los tiempos.

**Fase 4. Presentación** (`/presentacion`)
Construye las diapositivas siguiendo `guia-diseno.md` y `reglas-aprendidas.md`. Publica `presentacion.html` como artefacto y entrega a Gio el link y la ruta local.

**Fase 5. Ajustes**
Aplica los cambios de Gio y republica el artefacto (mismo link). Si una corrección vale para todas las clases, regístrala en `reglas-aprendidas.md` en ese mismo momento, sin preguntar.

**Fase 6. Cierre** (`/cerrar-clase`)
Después de dictada la clase: completa aprendizajes, frase ancla, compromiso, bucle abierto, términos y temas en `clase.json`; escribe `notas-publicas.md`; cambia el estado a `cerrada`. Pregunta a Gio solo por lo que no puedes saber (fecha real, cómo le fue, qué funcionó) y, si no responde, cierra con lo que hay.

## Presentaciones como artefactos

Cada presentación se publica tal cual, con el motor de cristal, como artefacto privado de claude.ai. Así Gio tiene un link fijo para revisarla desde cualquier dispositivo o compartirla. El archivo local sigue siendo la fuente y la copia de respaldo para proyectar.

- **Primera publicación** (Fase 4): herramienta Artifact con `file_path` = `clases/NNN-slug/presentacion.html`, `icon: "slides"` y una `description` de una frase. Guarda el link que devuelve en el campo `artefacto` de `clase.json` y anótalo en `historial`.
- **Republicar** (Fase 5, cierre o aviso del hook): mismo `file_path`, sin `icon`. En una conversación nueva pasa también `url` = el `artefacto` de `clase.json`, y antes lee el artefacto con `action: "read"`: sin eso la publicación se rechaza. Nunca publiques sin `url` una clase que ya tiene artefacto, porque crearía un link nuevo.
- **Recursos:** si las diapositivas usan `recursos/` (fotos o video, como la 002), agrégalos con `files`: `{"recursos/foto.jpg": "clases/NNN-slug/recursos/foto.jpg"}`. El límite es 15 MB por archivo.
- **Antes de publicar** revisa el contenido en `contenido.md` o en las diapositivas fuente, no en `presentacion.html` (bloqueado por tokens). Publicar distribuye el contenido: nada que no hayas visto.
- **Una vez por turno:** si editas varias diapositivas, republica una sola vez al final.
- El artefacto es privado. Solo Gio decide si lo comparte, desde el menú Compartir de la página.

## Continuidad entre clases

- Toda clase nueva abre con tres diapositivas automáticas que se escriben como tokens en `deck.json`:
  - `@pilares`: los 3 pilares, con el pilar de la clase resaltado. Los nombres salen de `pilares.json`.
  - `@repaso`: los aprendizajes y la frase ancla de la clase anterior, tomados de su `clase.json`.
  - `@seguimiento`: la pregunta por el compromiso de la clase anterior.
- Toda clase nueva lleva `@plataforma` antes de la frase ancla: la invitación a app.becoach.pro (todas las clases, guías prácticas, descargables, acceso gratuito). `@plataforma` es la versión oscura y `@plataforma:claro` la clara; elige la que siga mejor el ritmo de las diapositivas vecinas. El texto se cambia en un solo lugar: `PLATAFORMA` en `scripts/construir_presentacion.py`.
- Toda clase cierra con: compromiso concreto (con quién y cuándo), frase ancla, avance de la próxima clase (el bucle abierto) e invitación a traer a alguien de su equipo.
- Por eso `aprendizajes` (3), `frase_ancla`, `compromiso` y `bucle_abierto` de `clase.json` son obligatorios antes de cerrar.

## Memoria del proyecto: qué registrar sin que te lo pidan

- Correcciones de Gio que aplican siempre → `conocimiento/reglas-aprendidas.md`.
- Decisiones sobre el programa (nombres, formato, audiencia, lanzamiento) → `conocimiento/decisiones.md`, con fecha.
- Ideas de temas que Gio mencione de paso → `conocimiento/ideas-temas.md`.
- Todo lo de una clase concreta → su `clase.json` (el campo `historial` sirve para eventos importantes).

## Reglas firmes

- Nunca escribas a mano los nombres de los pilares en una diapositiva: usa `@pilares` o léelos de `pilares.json`. Los `id` no cambian aunque cambie el nombre (el pilar 3, Integración, conserva el id `sostenimiento`).
- En pantalla solo va lo que la audiencia necesita ver. Tiempos, indicaciones de chat, encuestas y guion van en el `<aside>` (notas del orador) de cada diapositiva.
- Contenido ontológico con rigor: distinciones claras (afirmaciones y juicios, declaraciones, pedidos y promesas, quiebres, estados de ánimo, observador), con ejemplos concretos. Cita fuentes en las notas cuando uses autores (Echeverría, Maturana, Kofman, Olalla, etc.).
- Tono: directo y confrontativo con respeto. "Hazte cargo" es una provocación que funciona para la audiencia, pero la clase enseña a los líderes a no usarla como orden con sus colaboradores.
- Sin fotos salvo las que Gio ponga en `clases/NNN-slug/recursos/`. Usa ilustraciones SVG con la paleta de la marca.

## Scripts disponibles

```bash
python scripts/estado.py                               # estado del programa
python scripts/nueva_clase.py "Título" --idea "..."    # crea la carpeta de una clase
python scripts/construir_presentacion.py 002           # construye una presentación (o --todas, o --muestra, o --catalogo)
python scripts/actualizar_indices.py                   # regenera bitácora, mapa de temas y glosario
python scripts/exportar_contenido.py 002              # exporta el contenido de una clase a contenido.md (o --todas)
```

## Próximos proyectos (ten en cuenta el formato)

- **Sitio web de las clases:** cada clase publicará su `presentacion.html` y su `notas-publicas.md`. Mantén estable la estructura de carpetas, el esquema de `clase.json` y el frontmatter de `notas-publicas.md`.
