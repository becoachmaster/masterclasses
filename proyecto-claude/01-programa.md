# Programa BeCoach: marco, estructura y reglas

> Generado por scripts/paquete_proyecto.py. Para cambiarlo, edita los archivos originales del repositorio.


---

<!-- Fuente: conocimiento/marco-programa.md -->

# Marco del programa

## Propósito
Clases semanales abiertas de coaching ontológico para líderes de equipo. El objetivo de esta etapa es **construir comunidad**: que las personas vuelvan cada semana, apliquen lo aprendido e inviten a otras personas.

Más adelante se lanzará un programa pago (este u otro). La decisión de cuándo lanzarlo es de Gio, cuando se sienta listo. Mientras tanto, las clases no incluyen oferta salvo que Gio lo pida.

## Audiencia
Líderes de equipo: jefes, coordinadores, supervisores, directivos y emprendedores con personas a cargo. Personas que viven la tensión de sacar resultados a través de otros y que muchas veces se sienten solas sosteniendo al equipo.

## Los 3 pilares del liderazgo personal
Los nombres viven en `pilares.json`.

1. **Responsabilidad personal:** hacerme cargo de lo que depende de mí. Pasar de víctima a protagonista.
2. **Conexión:** construir confianza, escucha y conversaciones que acercan al equipo.
3. **Integración:** llevar lo declarado a la práctica diaria y sostenerlo en el tiempo.

Cada clase pertenece a un pilar. La audiencia debe ver siempre el mapa completo y saber en qué pilar estamos.

## Método de cada clase: Comprender → Construir → Emerger
- **Comprender:** qué es, cómo se manifiesta, distinciones ontológicas.
- **Construir:** el cambio de observador del líder. Siempre empieza por el líder, no por el equipo.
- **Emerger:** la herramienta práctica y la conversación que transforma.

## Tono
- Directo, con alta convicción, confrontativo con respeto. Nada de motivación blanda.
- El líder también es parte del problema: cada clase lo pone frente al espejo.
- Rigor ontológico: distinciones claras y ejemplos concretos del día a día de un equipo.

## Mecanismos de comunidad y enganche
- Ritual de apertura repetido (pilares, repaso, seguimiento del compromiso).
- Compromiso concreto al final de cada clase, con nombre y fecha.
- Bucle abierto: cada clase termina con una pregunta que la siguiente responde.
- Invitación explícita a traer a alguien del equipo a la próxima clase.
- Lenguaje común que se acumula (ver `glosario.md`).


---

<!-- Fuente: conocimiento/pilares.json -->

```json
{
  "nota": "Fuente única de los nombres de los pilares. Los id no cambian aunque cambie el nombre (el id del pilar 3 sigue siendo 'sostenimiento').",
  "pilares": [
    {
      "id": "responsabilidad",
      "nombre": "Responsabilidad personal",
      "descripcion": "Hacerme cargo de lo que depende de mí y de cómo respondo a lo que pasa.",
      "icono": "Anchor",
      "provisional": false
    },
    {
      "id": "conexion",
      "nombre": "Conexión",
      "descripcion": "Construir confianza y conversaciones que acercan al equipo.",
      "icono": "Heart",
      "provisional": false
    },
    {
      "id": "sostenimiento",
      "nombre": "Integración",
      "descripcion": "Llevar lo declarado a la práctica diaria y sostenerlo en el tiempo.",
      "icono": "Cycle",
      "provisional": false
    }
  ]
}
```


---

<!-- Fuente: conocimiento/estructura-clase.md -->

# Estructura de cada clase (50 minutos por Zoom)

Vigente desde el 2026-11-05. Reemplaza la estructura de 8 bloques fijos, que hacía que todas las clases salieran iguales: las mismas preguntas, los mismos títulos y los mismos elementos, y que recortaba el material fuente para que cupiera en los moldes.

**La idea:** solo el ritual es fijo (cómo abre y cómo cierra la clase), porque crea comunidad y continuidad. El centro de la clase (unos 35 minutos) se diseña cada vez a partir del material fuente y de la pregunta guía. El tema decide la forma, no al revés.

## 1. El ritual fijo

| Momento | Tiempo | Qué lleva |
|---|---|---|
| Apertura | 4 a 5 min | `portada`, `@pilares`, `@repaso`, `@seguimiento` |
| Cierre | 5 a 6 min | Compromiso (con quién y cuándo), avance de la próxima clase (bucle abierto), invitación a traer a alguien del equipo, `@plataforma` y `ancla` |

Diapositivas obligatorias: `portada`, `@pilares`, `@repaso` y `@seguimiento` (desde la segunda clase), compromiso, próxima clase, invitación, `@plataforma` (o `@plataforma:claro`) y `ancla` (solo la frase ancla).

## 2. Lo que toda clase necesita (pero no en un orden fijo)

Son funciones, no bloques: pueden estar en cualquier orden, repetirse o fusionarse.

- **Un quiebre** que haga ver el problema en carne propia en los primeros minutos (pregunta con contexto concreto, dato que sacude, caso, escena, frase típica…).
- **Una pregunta guía** y un **modelo central** que la responde. El modelo lleva una diapositiva por elemento.
- **Un momento en que el líder se mira a sí mismo** (puede ser una encuesta, un espejo de frases, un dato contra el que compararse, una escena, una pregunta en silencio).
- **Algo práctico que se pueda usar el lunes** (herramienta, preguntas, conversación, protocolo).
- **Una práctica individual** conectada con el modelo (en papel, auto-observación).
- **Interacción cada 5 a 8 minutos**, con formatos que cambien (ver el banco de interacciones).

## 3. El centro flexible: elige un arco

Elige el arco que mejor sirve al material y a la pregunta guía. No repitas el arco de la clase anterior salvo que Gio lo pida. Puedes combinar dos.

| Arco | Forma | Sirve cuando… |
|---|---|---|
| **Problema → modelo → herramienta** | Duele algo, se explica por qué pasa, se da la salida | El tema tiene un mecanismo claro (la cadena de la reacción) |
| **Mito → evidencia → nueva mirada** | "Lo que creemos", datos que lo desmienten, la distinción que cambia el observador | El material trae datos o investigación que contradicen el sentido común |
| **Caso → disección → principio** | Un caso único (equipo, partido, escena) recorrido de principio a fin y luego generalizado | Hay un ejemplo reconocible y potente (la Selección 2014 en la 002) |
| **Mapa → zoom → aplicación** | Se muestra el panorama completo (un marco de 4 áreas, un mapa), se elige una zona y se profundiza | El tema es parte de un marco mayor (inteligencia emocional, dominios de la confianza) |
| **Dos observadores** | El mismo hecho visto desde dos lugares; la clase recorre el paso de uno a otro | La transformación es un cambio de mirada (víctima y responsable) |
| **Pregunta abierta → exploración → síntesis** | La clase avanza con preguntas al grupo y se construye el modelo con lo que aparece | El tema es más reflexivo que técnico (propósito, sentido) |
| **Serie** | Un elemento por bloque (los 4 estados de ánimo, los 3 dominios), cada uno con su propia mini-estructura | El modelo tiene partes que merecen su espacio |

Cada bloque del centro se nombra por lo que trata y termina con un puente hacia la pregunta guía.

## 4. Banco de movimientos (el repertorio, no una lista obligatoria)

Usa los que el material pida. Varía de una clase a otra: revisa en `mapa-temas.md` y en los `deck.json` de las dos clases anteriores cuáles se usaron, para no repetir los mismos.

- **Para abrir o sacudir:** pregunta con contexto · dato que sacude (`cifra`, gráfico) · escena o caso · frase típica en chat · "lo que creemos" · encuesta de entrada · micro-práctica corporal.
- **Para explicar:** distinción en dos columnas · modelo con diagrama · marco de 4 áreas (`cuadrante`) · línea de tiempo o proceso · tabla comparativa · cita de un autor · ejemplo único recorrido de principio a fin.
- **Para mostrar evidencia:** `cifra` · `barras` · `dona` · `tabla` · `pendiente` (antes y después) · estudio contado en una diapositiva.
- **Para que el líder se mire:** encuesta de autodiagnóstico · errores comunes con frases típicas · espejo de un dato ("el 95 % cree que…, ¿y tú?") · escala del 1 al 10 en el chat · pregunta en silencio.
- **Para llevar a la práctica:** pasos · preguntas · conversación modelo (reacción y respuesta) · antes y después de una frase · guion de una conversación · checklist.
- **Para practicar:** los formatos del banco de ejercicios (abajo).

## 5. Banco de interacciones (siempre en las notas, nunca en pantalla)

- Cascada en el chat: todos escriben y envían al mismo tiempo.
- Encuesta de Zoom con 2 a 4 opciones.
- Escala en el chat: "del 1 al 10, ¿cuánto…?".
- Una palabra en el chat.
- Reacciones de Zoom (pulgar, corazón) para un sí o no rápido.
- Micro-práctica corporal frente a la cámara (30 segundos).
- Pregunta en silencio con pausa (sin chat).
- Ejercicio individual en papel. No usar salas de grupos salvo que Gio lo pida.

## 6. Banco de formatos de ejercicio

- El espejo del líder: revisar una conversación real y rediseñarla.
- Traductor: reescribir frases de un modo a otro.
- Hecho o juicio: separar afirmaciones de interpretaciones.
- Carta no enviada, inventario de compromisos, mapa de conversaciones pendientes.
- Autoevaluación en un marco (puntuarse del 1 al 5 en cada área de un modelo y elegir una).
- Recorrer una situación propia con las preguntas del modelo.

## 7. Contra la repetición

Antes de proponer el temario, compara con las dos clases anteriores:
- **Títulos:** ninguna diapositiva repite el título de una diapositiva de las dos clases anteriores (salvo las automáticas y las obligatorias del cierre).
- **Preguntas:** el quiebre, la encuesta y la cosecha no usan la misma fórmula ("La última vez que…", "Cuando alguien de tu equipo…", "¿En qué pregunta se te movió algo?").
- **Plantillas:** ninguna plantilla se usa más de tres veces en la clase, salvo una serie (los elementos del modelo, las fases de la práctica).
- **Arco:** distinto del de la clase anterior.

## 8. Tiempos

No hay minutos fijos por bloque. Solo dos límites: el ritual suma unos 10 minutos y la práctica individual dura entre 6 y 10. El total no pasa de 50. Entre 25 y 38 diapositivas; las declaraciones, los datos y los divisores pasan rápido.


---

<!-- Fuente: conocimiento/reglas-aprendidas.md -->

# Reglas aprendidas

Correcciones de Gio que aplican a todas las clases. Claude agrega una línea cada vez que Gio corrige algo generalizable, sin esperar a que lo pida.

## Diapositivas
- 2026-11-26 · Estilo simple (sistema v2) para todas las clases nuevas: paleta azul + Brasa, composición centrada, tarjetas blancas, píldoras y círculos numerados (ver `guia-diseno.md` y `plantillas/slides-simple/`). Reemplaza al sistema de cristal en tierra, que queda solo en las clases 005 y 006.
- 2026-11-26 · Los colores dentro de los gráficos llevan degradado (tono → tono oscuro). El color plano queda para detalles que deben romper el patrón o notarse más: la línea de tendencia, el punto foco, una meta.
- 2026-11-26 · Vidrio desenfocado en tarjetas que van sobre fotos, patrones o ilustraciones, y en las tarjetas que contienen gráficos. No se agregan formas decorativas de fondo: se ven mal.
- 2026-11-02 · Todas las clases llevan la diapositiva `@plataforma` (app.becoach.pro: todas las clases, guías prácticas, descargables, acceso gratuito), oscura o clara según el contexto de las diapositivas vecinas.
- 2026-11-02 · (Reemplazada el 2026-11-26 por el estilo simple.) Sistema de cristal para todas las clases nuevas (ver `guia-diseno.md` y `plantillas/muestra/`): fondos oscuros siempre con degradado, tarjetas de cristal, un solo foco Brasa con brillo, más variedad de composiciones y alternancia de fondos oscuros y claros. El café ya no es fondo salvo casos puntuales.
- 2026-11-02 · La esquina superior derecha (x > 1360, y < 340) queda vacía: ahí va la cámara de Gio en el video editado. En la clase 4 la cámara tapó contenido de las diapositivas.
- 2026-09-24 · Sin pretítulos (etiquetas pequeñas en mayúsculas encima de los títulos). Tampoco dentro de las tarjetas: el título de la tarjeta dice lo que es.
- 2026-09-24 · Sin marcas de tiempo en pantalla (minutos, "fase 1 de 4 · 2 min").
- 2026-09-24 · Sin indicaciones de chat ni de encuesta en pantalla. Todo eso va en las notas del orador.
- 2026-09-24 · Más gráficos e ilustraciones en el estilo de la clase 001 (mensajes de chat, espejo, pozo, calendario), no fotos genéricas.
- 2026-09-24 · No usar fotos de talleres anteriores salvo que Gio las pida para esa clase.
- 2026-09-30 · Si una diapositiva amerita una foto que no existe, poner un mockup (recuadro punteado con "Imagen sugerida: …") y avisar a Gio para que la busque. Las fotos de Gio van en `recursos/` de la clase.
- 2026-09-24 · En los ejercicios guiados, si el texto habla por sí solo, sin título ("Trae la escena", "Cosecha" se eliminaron).
- 2026-09-24 · La diapositiva final lleva solo la frase ancla, sin imagen.
- 2026-09-24 · Los modelos (como O·A·R) llevan gráficos o íconos, no solo cajas de texto.
- 2026-09-29 · Sin historias personales ni anécdotas en las diapositivas: Gio las cuenta en vivo (en pantalla no se ven naturales ni genuinas). Pueden ir como recordatorio en las notas del orador.
- 2026-09-29 · Sí van en pantalla ejemplos de frases típicas y de situaciones que ocurren con frecuencia en los equipos ("Yo ya hice mi parte", "Eso no es mi área").
- 2026-09-24 · Las distinciones ontológicas se explican con datos y ejemplos concretos (ver "Hecho o interpretación" en la clase 001).
- 2026-11-05 · Más gráficos, tablas y datos con análisis: plantillas `barras`, `dona`, `tabla`, `pendiente` y `cuadrante` (traídas del sistema original de slides al de cristal). Fuente en pantalla y como máximo una diapositiva de datos de cada cuatro.

- 2026-11-05 · `@repaso` con menos texto: muestra el campo `repaso` de la clase anterior (los 3 aprendizajes en 8 palabras o menos). Si no existe, usa `aprendizajes`.

## Contenido
- 2026-09-29 · Confianza: se enseñan los tres dominios de Echeverría (sinceridad, competencia, confiabilidad). "Disponibilidad" no es un dominio. Si se menciona un cuarto (cuidado o compromiso con el otro), se atribuye a su autor (Feltman).
- 2026-09-29 · Las definiciones de trabajo (propósito, visión, valores, principios) se presentan como operativas, no canónicas, y cada una lleva un ejemplo concreto.

## Estructura de clase
- 2026-11-02 · No se usan las etiquetas Comprender, Construir y Emerger: ni en las diapositivas (sin divisores P.01, P.02, P.03), ni al presentarle a Gio el temario o la escaleta. Cada bloque se nombra por lo que trata.
- 2026-11-05 · La estructura de 8 bloques fijos hacía que todas las clases salieran iguales (mismas preguntas, títulos y elementos). Ahora solo el ritual de apertura y cierre es fijo; el centro se diseña con un arco elegido según el material (ver `estructura-clase.md`), distinto del de la clase anterior.
- 2026-11-05 · El material fuente de Gio no se recorta: se guarda completo en `fuente/` y se inventaría elemento por elemento en `fuente/inventario.md` con su destino (pantalla, notas, guía, banco de ideas, próxima clase). Nada se descarta sin su aprobación. Los datos, gráficos y tablas que traiga se muestran con las plantillas de datos.
- 2026-11-02 · Cuando Gio entrega material (talleres, documentos, propuestas con estructura propia), es fuente de contenido, no un guion: la clase se diseña con el método del programa, pero todo el material queda inventariado (regla anterior).
- 2026-09-29 · Cada clase tiene una pregunta guía (se formula en la gran idea) y un modelo central. Todo concepto, el observador del líder y los errores deben abrir paso a responder esa pregunta; Emerger entrega la respuesta práctica.
- 2026-09-29 · No introducir conceptos que no se usen después. (2026-11-05: se quita el tope de dos marcos teóricos; lo que no se use en pantalla va a notas, guía o próxima clase.)
- 2026-09-29 · Un ejemplo único, reconocible para la audiencia, aplicado al modelo de principio a fin (en la 002, la Selección Colombia 2014). Solo datos verificables en pantalla.
- 2026-09-29 · El ejercicio se conecta con el modelo de la clase.
- 2026-09-30 · Si el ejercicio compara dos momentos (hoy y deseado), ambas fases usan el mismo formato (por ejemplo, tres palabras y tres palabras) para que la comparación sea directa. Lo complejo (el borrador completo del modelo) va al compromiso con el equipo, no al papel individual.
- 2026-09-30 · El modelo central lleva una diapositiva por elemento. Si falta tiempo, se recortan otros temas, nunca el modelo.
- 2026-09-30 · El nombre del modelo no puede repetir el de una de sus partes (en la 002, "identidad" era a la vez el todo y un elemento; el todo pasó a llamarse brújula del equipo).
- 2026-09-29 · Evaluar la secuencia como alguien que viene a aprender: cada bloque responde una pregunta del participante y termina con un puente hacia la pregunta guía.
- 2026-09-24 · Sin ejercicios en tríadas ni salas de grupos: los ejercicios son de auto-observación individual guiada por Gio.
- 2026-09-24 · Primero cambia el observador del líder, después la técnica de conversación.
- 2026-09-29 · El corazón de la clase es el momento en que el líder se observa a sí mismo. (2026-11-05: el autodiagnóstico con encuesta y los errores comunes con frases típicas son opciones del repertorio, no obligatorias en cada clase: se estaban repitiendo. Alterna con un dato espejo, una escala en el chat, una escena o una pregunta en silencio.)

## Redacción
- Español neutro/colombiano con tuteo. Nunca voseo.
- 2026-10-14 · Las clases son talleres para líderes de equipo, no formación para coaches: explica los fundamentos ontológicos con palabras cotidianas y ejemplos de gestión, sin acumular tecnicismos ni presentar las etiquetas como errores antes de explorar su efecto. Pon el mensaje central al inicio y conserva solo conceptos que ayuden a actuar.
- 2026-10-14 · Las preguntas de apertura deben dar contexto concreto para que la audiencia pueda recordar una situación y responder; evita pedir una reflexión abstracta sin marco.

## Recordatorios de la clase
- 2026-10-29 · Las plantillas de los recordatorios ya incluyen hora, enlace e instrucciones. Claude solo escribe el contenido de la clase: qué se aprende y qué resultados se llevan. Cada mensaje cumple una función: 6:00 p. m. acompaña el envío del enlace; 6:45 p. m. anuncia que la sala está abierta; 7:00 p. m. anuncia que comenzamos y crea urgencia.


---

<!-- Fuente: conocimiento/decisiones.md -->

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

## 2026-11-26 · Marca v2: azul + Brasa y estilo simple
- La paleta pasa de tierra y café a **azul** (`#1E2A4E`, el color del logo) y se mantiene la **Brasa** (`#FF5A1F`) como foco. Estilo Mac limpio. El manual de marca completo vive en el sistema de diseño «BeCoach» en claude.ai (https://claude.ai/artifact/JR6WZ7PAx5Fm2hGApZk4Jt).
- Las presentaciones nuevas usan el **estilo simple** (`"estilo": "simple"` en `deck.json`), adaptado del taller de marketing con IA: composición centrada, títulos grandes, tarjetas blancas, píldoras, círculos numerados y tablas con encabezado azul. Motor: `motor/simple.css`; plantillas: `plantillas/slides-simple/`.
- Las clases 005 y 006 conservan el sistema de cristal en tierra (`"estilo": "cristal"`), y las 001 a 004 su estilo original.
- Se sigue usando el motor propio (no el tipo «Slides»): conserva `@pilares`, `@repaso`, `@seguimiento`, `@plataforma`, las notas del orador y la zona de la cámara.
- Gráficos con paleta de datos propia (azul de datos, Brasa, turquesa), con degradado en barras, segmentos, áreas y celdas; máximo tres series.
- El **vidrio desenfocado** se usa en tarjetas sobre fotos, patrones o ilustraciones. No se agregan formas de fondo solo para lucirlo: Gio las probó y no van.

