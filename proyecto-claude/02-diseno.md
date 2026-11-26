# Diseño de las presentaciones

> Generado por scripts/paquete_proyecto.py. Para cambiarlo, edita los archivos originales del repositorio.


---

<!-- Fuente: conocimiento/guia-diseno.md -->

# Guía de diseño de las diapositivas · estilo simple (sistema v2)

Vigente desde el 2026-11-26. Marca: **azul** (`#1E2A4E`, el color del logo) como base y **Brasa** (`#FF5A1F`) como foco, con estilo Mac limpio. El manual de marca completo (logo, paleta, tipografía, aplicaciones, impresión) es el sistema de diseño «BeCoach» en claude.ai: https://claude.ai/artifact/JR6WZ7PAx5Fm2hGApZk4Jt. Esta guía solo cubre las diapositivas.

En `deck.json` va `"estilo": "simple"`. Motor: `motor/simple.css`. Plantillas: `plantillas/slides-simple/`; todas juntas en `plantillas/catalogo-simple.html?zona`. Las clases 005 y 006 siguen en el sistema de cristal (`guia-diseno-cristal.md`); las 001 a 004, en su estilo original.

## Lienzo y composición
- Cada diapositiva es un `<section>` de 1920 × 1080 con `class="s"` (fondo claro) o `class="s az"` (fondo azul). El contenido va en columna, con `gap` entre bloques; no se posiciona con `position:absolute` salvo casos puntuales.
- **Títulos centrados o a la izquierda, según la diapositiva.** Centrado (por defecto) para portada, pilares, declaraciones, citas, compromiso, divisores, comparaciones y la frase ancla. A la izquierda (`class="s izq"`) para tablas, gráficos de lectura horizontal y diapositivas con mucho contenido; ahí el bloque se apoya abajo y el título puede medir hasta 1200 px.
- Estructura típica: título (`h2`) → contenido (tarjetas, tabla o gráfico) → una línea de apoyo o una píldora.
- Alterna fondos claros y azules para dar ritmo. Portada, datos destacados, compromiso, divisores y declaraciones van bien en azul.
- Los elementos entran uno tras otro al llegar a la diapositiva: agrega `class="rise"` y `style="--i:N"` (N = orden).

## La esquina de la cámara (regla firme)
La zona **x > 1360 px, y < 340 px queda vacía**. Por eso los títulos centrados miden como máximo **800 px** (`h2` ya lo trae); los títulos a la izquierda no llegan a la zona y miden hasta 1200 px. Si el contenido es alto, el título sube; mantén el bloque principal por debajo de y = 340 cuando sea más ancho que 800 px. Compruébalo siempre con `presentacion.html?zona`.

## Paleta
| Nombre | Hex | Uso |
|---|---|---|
| Azul | `#1E2A4E` | Fondos azules, encabezados de tabla, círculos, píldoras, tarjeta azul |
| Azul bajo / noche | `#121A33` / `#0A0F1F` | Final de los degradados azules |
| Azul acero | `#3D5A8C` | Íconos y etiquetas sobre claro |
| Azul hielo | `#A9BEE0` | Íconos y etiquetas sobre azul |
| Azul bruma | `#DCE4F0` | Píldora suave, fondo de barras |
| Brasa / Brasa alta | `#FF5A1F` / `#FF7A45` | El foco (una vez por diapositiva) |
| Brasa profunda | `#C43A08` | Brasa como texto sobre claro |
| Tinta / Tinta suave | `#141B2D` / `#4E5A70` | Texto sobre claro |
| Nube / Gris hielo | `#F5F7FA` / `#A9B4C8` | Texto sobre azul |

- **Un solo foco Brasa por diapositiva**: la tarjeta `foco` o `brasac`, el círculo `brasa-b`, la píldora `brasa-p` o la palabra `foco-t`.
- Texto sobre Brasa en **tinta**, nunca en blanco. Brasa como texto sobre claro, en Brasa profunda (`foco-t` lo hace solo).
- **Degradados de dos tonos de la misma familia**, del tono a su paso más oscuro. Nunca se mezclan azul y Brasa en un degradado.
- La frase ancla no lleva Brasa.

## Piezas (clases de `motor/simple.css`)
| Clase | Qué es |
|---|---|
| `card` | Tarjeta blanca Mac (radio 28, borde fino, sombra suave) |
| `card vidrio` | **Vidrio desenfocado**: deja ver, borroso, lo que hay detrás. Úsalo sobre fotos, patrones o ilustraciones, y en las tarjetas que contienen gráficos y tablas |
| `card foco` | Tarjeta con borde y halo Brasa |
| `card brasac` / `card azulc` | Tarjeta rellena en Brasa (foco) o en azul (destaca sin gastar el foco) |
| `card tabla` | Contenedor de tabla; la fila `tr.th` es el encabezado azul |
| `pill`, `pill soft`, `pill white`, `pill brasa-p`, `pill linea` | Píldoras: azul, suave, blanca (sobre azul), Brasa y punteada |
| `badge`, `badge brasa-b`, `badge hielo` | Círculo numerado o con ícono |
| `phone`, `screen`, `bubble`, `bubble ult` | Teléfono con mensajes (la última burbuja en Brasa) |
| `grid2`, `grid3`, `row`, `col` | Distribución |
| `lead`, `small`, `foco-t`, `serif` | Texto de apoyo, nota, palabra foco, cita |
| `puntos` | Patrón de puntos pequeño, abajo a la izquierda |

**No se agregan formas decorativas de fondo** (círculos, manchas, anillos) solo para lucir el vidrio: Gio las probó y se ven mal.

## Tipografía
Manrope en todo, pesos 500 a 800; Fraunces itálica solo en citas. `h1` 132 px, `h2` 72 px (portada y ancla hasta 112 px), `h3` 40 px, texto 32 px, `lead` 40 px, `small` 26 px. **Nunca menos de 24 px.**

## Gráficos
- **Paleta de datos**, máximo **tres series**: azul de datos `#3366CC` (degradado `#4A80E4 → #2852B0`), Brasa (`#FF7A45 → #F04E14`) para la serie o el dato foco, y turquesa `#1D9A8A` (`#1FA38F → #167E70`). Más de tres: agrupa en «Otros» o divide en gráficos pequeños.
- Barras, segmentos, áreas y celdas llevan **degradado**. El **color plano** queda para los detalles que deben romper el patrón: línea de tendencia, punto foco, una meta.
- Las líneas van en trazo plano de 5 px; el área en degradado va solo bajo la serie foco.
- Escala secuencial (mapa de calor): un solo tono, de `#E8EDF4` a `#1E2A4E`.
- Leyenda siempre que haya dos series o más, con rótulos directos selectivos (primer y último valor, el foco). El texto va en tinta, nunca del color de la serie.
- El gráfico va dentro de una `card vidrio`, con la **fuente en pantalla** y solo datos verificables. Como máximo una diapositiva de datos de cada cuatro.
- **Los gráficos funcionan en claro y en azul.** El mismo SVG cambia de colores según la sección: textos y ejes en blanco y gris hielo, azul y turquesa de datos más luminosos (`#7BA4F2`, `#3CC6B1`) y la escala del mapa de calor invertida (de oscuro a claro). Para que funcione, el SVG usa clases (`tx`, `ts`, `tf`, `gr`, `ax`, `pista`, `anillo`, `h0`–`h5`) y los degradados `var(--g-…)`: copia la estructura de una plantilla `grafico-*` en vez de poner colores fijos.

| Lo que quieres mostrar | Plantilla |
|---|---|
| Un dato real con su fuente | `cifra-barras` |
| Cambio en el tiempo, una serie | `grafico-barras` |
| Comparar dos grupos por categoría | `grafico-agrupadas` |
| Ordenar motivos o causas | `grafico-ranking` |
| Tendencia de dos series | `grafico-lineas` |
| Relación entre dos variables | `grafico-dispersion` |
| Partes de un total (máximo 3) | `grafico-dona` |
| Partes de un total por grupo | `grafico-apiladas` |
| Intensidad en una cuadrícula | `grafico-calor` |
| Tres indicadores con tendencia | `grafico-indicadores` |
| Comparar en filas | `tabla` |
| Seguimiento de compromisos | `tablero` |

## Plantillas (`plantillas/slides-simple/`)
`portada`, `pregunta` (teléfono), `comparacion`, `declaracion`, `tres-columnas`, `pasos`, `modelo`, `tabla`, `tablero`, `checklist`, `cita`, `divisor`, `compromiso`, `invitacion`, `ancla`, `cifra-barras` y los `grafico-*`. Las automáticas (`@pilares`, `@repaso`, `@seguimiento`, `@plataforma`) las genera `construir_presentacion.py` en este mismo estilo.

## Ilustraciones e imágenes
- SVG propios con la paleta, como mínimo cinco por clase, que representen la idea (teléfono con mensajes, calendario, círculos que se cruzan, ciclo).
- Íconos de trazo redondeado: azul acero sobre claro, azul hielo sobre azul; solo el del foco en Brasa.
- Fotos solo las de Gio. Si una tarjeta va encima de una foto, usa `card vidrio`.

