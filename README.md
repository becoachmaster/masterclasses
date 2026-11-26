# BeCoach · Clases semanales de liderazgo

Sistema para diseñar, construir y registrar las clases semanales abiertas de coaching ontológico para líderes de equipo, trabajando con Claude Code.

## Cómo empezar
1. Descomprime la carpeta donde guardas tus proyectos.
2. Recomendado: conviértela en repositorio git para tener historial (`git init && git add . && git commit -m "Inicio del proyecto"`).
3. Abre una terminal en la carpeta y ejecuta `claude`.
4. Claude recibe automáticamente el estado del programa al iniciar la sesión.

Requisitos: Claude Code y Python 3 (solo librería estándar, sin instalar nada más).

## Comandos
| Comando | Para qué |
|---|---|
| `/nueva-clase <idea central>` | Arranca una clase nueva: cierra la anterior si hace falta y propone el enfoque |
| `/presentacion` | Construye o ajusta las diapositivas de la clase en curso |
| `/cerrar-clase [número] [cómo fue]` | Registra aprendizajes, frase ancla, compromiso y notas públicas |
| `/sugerir-temas` | Propone los próximos temas o secuencias según lo ya trabajado |
| `/estado` | Muestra en qué va el programa |
| `/renombrar-pilar <id> <nombre>` | Cambia el nombre de un pilar (el tercero es provisional) |

También puedes hablarle normalmente: "Hagamos la clase de esta semana sobre la confianza" funciona igual que `/nueva-clase`.

## Presentar la clase
Cada presentación se publica como artefacto privado en claude.ai. El link está en el campo `artefacto` de su `clase.json` y Claude lo republica en cada ajuste, así que siempre muestra la última versión.

Para proyectar en Zoom también puedes abrir `clases/NNN-slug/presentacion.html` en Chrome.
- **F:** pantalla completa.
- **P:** abre la vista de presentador en otra ventana (notas, siguiente diapositiva y reloj). Comparte en Zoom solo la ventana de la presentación.
- **← →, espacio o clic:** navegar. Funciona con presentadores inalámbricos.

## Lo que se actualiza solo
- Al iniciar la sesión, Claude recibe el estado del programa.
- Al editar un `clase.json`: bitácora, mapa de temas y glosario se regeneran; se reconstruyen las presentaciones afectadas.
- Al editar diapositivas: se reconstruye `presentacion.html` y se revisan las reglas de estilo.
- Durante el trabajo, Claude registra tus correcciones, decisiones e ideas de temas en `conocimiento/`.

## Estructura
```
CLAUDE.md                 Instrucciones de trabajo para Claude
conocimiento/             Base de conocimiento del programa
clases/NNN-slug/          Una carpeta por clase
  clase.json              Registro estructurado (fuente de verdad)
  escaleta.md             Minuto a minuto
  slides/                 Una diapositiva por archivo + deck.json
  recursos/               Fotos o archivos propios de la clase
  presentacion.html       Presentación lista para proyectar (generada)
  notas-publicas.md       Resumen para la comunidad y el sitio web
motor/                    Motor de presentación (CSS, JS, plantilla)
plantillas/               Plantillas de clase y de diapositivas
scripts/                  Automatizaciones
```
