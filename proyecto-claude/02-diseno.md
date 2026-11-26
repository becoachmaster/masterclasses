# Diseño de las presentaciones

> Generado por scripts/paquete_proyecto.py. Para cambiarlo, edita los archivos originales del repositorio.


---

<!-- Fuente: conocimiento/guia-diseno.md -->

# Guía de diseño de las diapositivas · sistema de cristal azul

**Marca vigente: manual de marca BeCoach v2.1 (2026-11-26), https://marca.becoach.pro** (repositorio `C:/Dev/becoach-marca`). La marca pasó de tierra y café al azul y mantiene la Brasa como foco. Si algo de esta guía choca con el manual, manda el manual. Los colores y las clases de superficie del motor (`motor/deck.css`) los escribe el bloque de marca desde el manual.

Historia: el sistema de cristal se aprobó el 2026-11-02 en la hoja de estilo de Claude Design (https://claude.ai/artifact/ALjaZrUvvRGoYaHRoWnbsw); el 2026-11-26 pasó a la paleta azul. Es el mismo sistema de los gráficos de video y de los reels: lo que se ve en la clase en vivo, en el video editado y en redes es una sola marca.

**La referencia viva es `plantillas/muestra/`**: la clase 4 rehecha en este sistema (`presentacion.html` y una diapositiva por archivo en `slides/`). Antes de construir una presentación, abre la muestra en Chrome (`plantillas/muestra/presentacion.html?zona`) y copia de `plantillas/slides/` el tipo que necesitas. **Las clases 001 a 006 ya se dictaron y conservan la marca v1 (tierra y café)**: su `deck.json` lleva `"marca": "v1"` y se construyen con `motor/deck-v1.css`. Las plantillas más viejas están en `plantillas/slides-v1/`.

## Lienzo
- Cada diapositiva es un `<section>` de 1920 × 1080 px. El fondo va como **clase** del `<section>` (`class="fondo"`); el resto, con estilos en línea.
- `deck.json` lleva `"estilo": "cristal"`: así `@pilares`, `@repaso` y `@seguimiento` salen en el mismo sistema. No lleva `"marca"` (eso es solo para las clases v1).
- Composición con `position:absolute` desde el borde: margen izquierdo 110 px, borde derecho 1810 px, título arriba en `top:96px`.
- Notas del orador dentro de `<aside>…</aside>` al final de cada `<section>`.

## La esquina de la cámara (regla firme)
En el video editado, la cámara de Gio va arriba a la derecha. **La zona x > 1360 px, y < 340 px queda vacía en todas las diapositivas.** Los títulos de arriba miden como mucho 1200 px de ancho; las tarjetas que llegan al borde derecho empiezan en `top:345px` o más abajo. Para comprobarlo, abre `presentacion.html?zona`: la zona se marca en naranja.

## Fondos (siempre con degradado de dos tonos de la misma familia, nunca planos)
| Clase | Uso |
|---|---|
| `fondo` | Oscuro principal: azul → azul noche, con brillo de azul luz arriba a la izquierda. Sin Brasa en el fondo |
| `fondo-profundo` | Oscuro alterno: azul bajo → azul noche. Divisores, repaso, estilos bajo presión, cierre (`fondo-mineral` sigue funcionando como alias) |
| `fondo-claro` | Claro Mac: nube → nube baja, con brillo blanco. Modelo central, comparaciones, práctica y frase ancla |
| `fondo-niebla` | Claro azulado: preguntas de apertura |

Alterna oscuros y claros para dar ritmo. La Brasa nunca va dentro de un fondo: solo como `halo` detrás del foco.

## Tarjetas
| Clase | Qué es |
|---|---|
| `cristal` | Tarjeta de cristal sobre oscuro: translúcida, borde fino, luz arriba y sombra profunda |
| `cristal cristal-opaco` | Cristal que tapa lo de atrás (nodos de un diagrama encima de líneas) |
| `claro` | Tarjeta blanca Mac sobre fondos claros, borde de 1 px y sombra suave |
| `azul` | Tarjeta azul sólida (azul → azul bajo): destaca sobre claro sin gastar el foco |
| `vidrio` | Cristal con desenfoque real del fondo; solo sobre fotos o video |
| `panel` | Panel interior oscuro dentro de una tarjeta de cristal |
| `baldosa` | Fondo de ícono (88 a 120 px): blanco → azul bruma sobre claro, cristal sobre oscuro |
| `foco` | Se suma a `cristal` o `claro`: borde y halo Brasa. Es el foco |
| `brasa` | Tarjeta rellena de Brasa (brasa alta → brasa); el texto encima va en tinta `#141B2D`, nunca en blanco |
| `brillo` | Texto Brasa con resplandor (la palabra clave sobre oscuro); `brillo-claro` sobre claro (Brasa profunda) |
| `halo` | Luz Brasa difusa detrás del foco (`<div class="halo" style="left…; top…; width…; height…">`) |
| `serif` | Fraunces itálica, **solo** para citas (la voz de otra persona o de la clase anterior) |

Radio 28 px como máximo (Gio no quiere bordes más redondeados). Íconos dentro de una baldosa de 88 a 120 px con radio 24 a 28.

## Uso de Brasa
- **Un solo foco por diapositiva**: la tarjeta `foco`, la tarjeta `brasa`, la palabra `brillo` o el elemento central de la ilustración. Un grupo con el mismo rol (los números 1, 2, 3 de una lista de pasos) cuenta como uno. La Brasa no pasa del 10 % de la diapositiva.
- Sobre oscuro: `#FF5A1F` en texto (sobre azul bajo o azul noche; sobre azul solo desde 24 px), íconos y rellenos. Sobre claro: Brasa solo como relleno (`brasa`); en texto usa Brasa profunda `#C43A08`.
- Los íconos y números repetidos van en azul hielo `#A9BEE0` sobre oscuro y en azul acero `#3D5A8C` sobre claro.
- La frase ancla de cierre no lleva Brasa.

## Paleta (del manual; detalle y contrastes en https://marca.becoach.pro)
| Nombre | Hex | Uso |
|---|---|---|
| Azul | `#1E2A4E` | La marca y el logo; inicio de los fondos oscuros y tarjetas azules |
| Azul bajo / azul noche | `#121A33` / `#0A0F1F` | Final de los degradados y fondos oscuros |
| Azul luz | `#3A5A9A` | Solo como brillo radial de los fondos oscuros |
| Brasa | `#FF5A1F` | El foco |
| Brasa profunda | `#C43A08` | Brasa para texto sobre claro |
| Azul hielo | `#A9BEE0` | Acento secundario sobre oscuro: íconos, números, flechas, etiquetas de ejes |
| Azul acero | `#3D5A8C` | Íconos, números y detalles sobre claro |
| Azul bruma | `#DCE4F0` | Tinte de alivio sobre claro (baldosas, celdas resaltadas) |
| Texto sobre oscuro | nube `#F5F7FA` y gris hielo `#A9B4C8` | Principal y secundario |
| Texto sobre claro | tinta `#141B2D` y tinta suave `#4E5A70` | Principal y secundario |
| Línea | `#D7DEE8` | Bordes de 1 px y tablas sobre claro |

## Logo
Logotipo azul sobre claro y blanco sobre oscuro, arriba o abajo a la izquierda, **nunca en la zona de la cámara** y nunca en Brasa. Archivos: `https://marca.becoach.pro/assets/logos/`.

## Tipografía
- Manrope en todo (`font-family:'Manrope', Arial, sans-serif`), pesos 500 a 800. El motor la incrusta: funciona sin internet.
- Títulos: 76 a 100 px, peso 800, `letter-spacing:-2.5px`, `line-height:1.04`.
- Declaraciones y portada: 112 a 136 px.
- Texto de tarjetas: 32 a 56 px. Apoyo: 28 a 44 px. **Nunca menos de 24 px.**

## Tipos de diapositiva (`plantillas/slides/`)
| Plantilla | Para qué | En la muestra |
|---|---|---|
| `portada` | Título abajo a la izquierda, marca arriba, ilustración orbital | `portada` |
| `divisor` | Folio gigante con contorno, título del bloque y avance de los 4 bloques | `p01`–`p04` |
| `pregunta` | Pregunta de apertura en claro con ilustración | `quiebre-nace`, `quiebre-reunion` |
| `declaracion` | Una frase central con la palabra clave en `brillo` | `respuesta`, `gran-idea` |
| `comparacion` | Dos tarjetas de cristal con panel, la segunda `foco` | `emocion-estado` |
| `comparacion-clara` | Dos tarjetas en claro, la segunda `brasa` | `se-entrena` |
| `plano-dos-ejes` | Cuatro tarjetas en un plano con ejes etiquetados | `estilos-caracteristicas`, `estilos-sombras` |
| `modelo` | El modelo central 2 × 2 en claro | `modelo` |
| `detalle-estado` | Un elemento del modelo: definición, frase típica, señales y su lugar en la matriz | `resentimiento` … `ambicion` |
| `diagrama-flujo` | Causa → señales → efectos, con retorno | `contagio` |
| `opciones` | Opciones A-D de una pregunta para votar | `autodiagnostico` |
| `frases` | Frases típicas en burbujas de chat y lo que provocan | `errores` |
| `tres-columnas` | Tres caminos o salidas, la última `foco` | `salir` |
| `pasos` | Lista numerada con diagrama a la derecha | `tres-preguntas` |
| `convergencia` | Varios elementos que apuntan a una meta | `alinear` |
| `practica` | Pregunta del ejercicio con número fantasma | `fase1`–`fase3` |
| `compromiso` | Pregunta de compromiso con calendario de cristal | `compromiso` |
| `invitacion` | Invitación con el puesto libre | `invitacion` |
| `cifra` | Un dato grande con su fuente en pantalla (solo datos verificables) | — |
| `barras` | Comparar magnitudes: hasta 6 barras horizontales, una en Brasa | — |
| `dona` | Cómo se reparte un total: hasta 3 partes, la parte foco en Brasa y su cifra en el centro | — |
| `tabla` | Cifras que no ganan nada dibujadas o que comparan columnas: hasta 4 × 5 | — |
| `pendiente` | Antes → después: qué subió y qué bajó, una recta por categoría | — |
| `cuadrante` | Un marco de 4 áreas en dos ejes (por ejemplo, los dominios de la inteligencia emocional) | — |
| `columnas` | Categorías con orden propio (años, opciones de una encuesta): hasta 6 | — |
| `lineas` | Evolución en el tiempo de hasta 4 series | — |
| `area` | Evolución de una sola serie (un registro de 7 días, un hábito) | — |
| `apilado` | Cómo se reparte un total, comparado entre momentos o grupos | — |
| `medidor` | Un valor contra su techo o su meta (22 de 100) | — |
| `dispersion` | La relación entre dos variables, un punto por caso. Úsala poco | — |
| `cita` | Una cita textual sola, en serif, con autor y obra | — |
| `lista` | Puntos sin orden, hasta 6, con la entrada en negrita | — |
| `checklist` | Verificaciones que se marcan, hasta 6, la última en Brasa | — |
| `@plataforma` | Automática: invitación a app.becoach.pro con la ventana de la plataforma. `@plataforma:claro` para la versión clara | `@plataforma` |
| `ancla` | Solo la frase ancla, en claro, sin Brasa | `ancla` |

Ritmo: no repitas la misma plantilla tres veces seguidas salvo una serie (los cuatro estados, las tres fases). Mezcla oscuro y claro.

## Datos, gráficos y tablas
Vienen del sistema original de slides (`Programacion/slides/_formato-tabla.md`), adaptados al cristal. Elige la forma por lo que el dato tiene que decir:

| Lo que quieres mostrar | Plantilla |
|---|---|
| Un número que sacude | `cifra` |
| Un valor contra su meta o su techo | `medidor` |
| Comparar varias magnitudes (nombres largos) | `barras` |
| Comparar categorías con orden propio (años, opciones) | `columnas` |
| Cómo se reparte un total | `dona` (un total) · `apilado` (varios totales comparados) |
| Varias cifras en columnas | `tabla` |
| Un cambio entre dos momentos | `pendiente` |
| Evolución en el tiempo | `lineas` (varias series) · `area` (una sola) |
| Relación entre dos variables | `dispersion` |
| Un marco de cuatro partes | `cuadrante` |

Todas están en `plantillas/catalogo.html` (se construye con `python scripts/construir_presentacion.py --catalogo`). Las plantillas cuyo pie dice "Datos de ejemplo" traen números inventados para mostrar la forma: nunca llegan así a una clase.

- **Solo datos verificables, con la fuente en pantalla** (autor o institución y año), en 26 px y gris al pie.
- **Escala honesta:** con porcentajes, la barra mide el porcentaje real (0 a 100). Nunca se recorta el eje para exagerar.
- **Un solo foco:** una barra, una parte o una cifra en Brasa; las demás en azul hielo (oscuro) o azul acero (claro).
- **Topes:** 6 barras, 3 partes de dona, 4 series de pendiente, tabla de 4 columnas × 5 filas. Si sobran categorías, agrupa en "Otros".
- **Ritmo:** como máximo una diapositiva de datos de cada cuatro; un gráfico detrás de otro no se lee.
- **El título dice la conclusión**, no el tema ("4 de cada 10 personas pasan el día con estrés", no "Estrés laboral").
- Si el material de Gio trae un gráfico como imagen, guárdalo en `recursos/` y redibújalo con estas plantillas; si no se puede, muéstralo dentro de una tarjeta `claro` con su fuente.

## Redacción en pantalla
Traídas del sistema original de slides:
- **Una idea por diapositiva.** Si tiene dos, pártela en dos.
- **El título afirma, no etiqueta.** En comparaciones, modelos y datos, el título es una afirmación que se pueda discutir ("La disciplina no desactiva el miedo"), no el nombre del tema ("Disciplina").
- **El texto de apoyo suma, no repite.** Si el título dice "Tu cerebro te protege del cambio", el apoyo no dice "Por eso te cuesta avanzar": agrega el dato, el mecanismo o la fuente ("La amígdala trata una amenaza al estatus como un peligro físico").
- **En pantalla nunca se describe la imagen.** Lo que se ve lo muestra el dibujo y lo que se dice va en las notas.
- **Las notas añaden, no leen.** No repiten lo que está en pantalla: llevan el ejemplo largo, la transición, la acción ("abre la encuesta") y la respuesta a la objeción que siempre sale.
- **Claro y oscuro cuentan la historia:** oscuro para el problema y la tensión, claro para el método y la salida. El paso de uno a otro coincide con el giro del argumento.

## Ilustraciones
- SVG en línea con trazo redondeado (`stroke-linecap:round`) en azul hielo (oscuro), azul acero (claro) o Brasa (solo el foco), dentro de baldosas o tarjetas de cristal. Se hacen con divs de cristal y formas simples (órbitas, mesas, calendarios, matrices), no con dibujos planos sueltos.
- Deben representar la idea (la mesa de la reunión, el puesto libre, la mini matriz que ubica cada estado), no decorar.
- Siguen disponibles `<x-icon name="…">` (Search, Users, CheckCircle, Key, Chat, Warning, Trust, Anchor, Heart, Cycle, Lightbulb, Target, Eye, Calendar, Compass, Mirror).

## Fotos y video
- Fotos y videos de Gio en `clases/NNN-slug/recursos/`, referenciados como `recursos/<archivo>`. Encima de una foto, la tarjeta es `vidrio`.
- Si falta una foto: recuadro punteado con "Imagen sugerida: …".
- Video: `<video src="recursos/x.mp4" controls preload="metadata" playsinline>`, sin autoplay.

## Lo que nunca va en pantalla
Ver `reglas-aprendidas.md`. En resumen: pretítulos (etiquetas pequeñas encima del título), tiempos, indicaciones de chat o encuestas, fases del ejercicio con minutos y cualquier texto para el orador.

