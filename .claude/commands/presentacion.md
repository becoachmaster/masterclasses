---
description: Construye o ajusta las diapositivas de la clase en curso (Fase 4 y 5), incluidos gráficos, tablas y datos. Úsalo siempre que Gio pida diapositivas, cambios visuales, agregar conceptos, gráficos o datos a una clase.
argument-hint: [número de clase, opcional]
---
Clase: $ARGUMENTS (si está vacío, la clase en curso).

## Antes de construir
1. Confirma que la escaleta está aprobada. Si no, termina primero la Fase 3.
2. Lee `conocimiento/guia-diseno.md` y `conocimiento/reglas-aprendidas.md`. Si la clase tiene `fuente/inventario.md`, léelo: todo lo marcado "pantalla" debe aparecer en alguna diapositiva, y todo lo marcado "notas" en algún `<aside>`.
3. Elige la plantilla por lo que la idea necesita, no por costumbre. Mira el catálogo de `guia-diseno.md` y abre solo las 2 o 3 plantillas de `plantillas/slides/` que vas a usar. La muestra completa está en `plantillas/muestra/presentacion.html?zona`.

## Construir
4. Una diapositiva por archivo en `slides/<id>.html`; el orden en `slides/deck.json` con `"estilo": "cristal"`. Empieza con `portada`, `@pilares`, `@repaso`, `@seguimiento`; termina con compromiso, próxima clase, invitación, `@plataforma` (o `@plataforma:claro`) y `ancla`.
5. Deja libre la esquina de la cámara (x > 1360, y < 340): ahí va Gio en el video.
6. Notas del orador en `<aside>`: tiempo, interacción, guion y fuentes. En pantalla solo lo que la audiencia necesita ver.
7. Ilustraciones SVG propias de la clase (al menos cinco). Representan la idea, no decoran.
8. **Datos:** cuando el material trae cifras, muéstralas. Elige el gráfico con la tabla "Lo que quieres mostrar" de `guia-diseno.md` (cifra, medidor, barras, columnas, dona, apilado, tabla, pendiente, líneas, área, dispersión, cuadrante). Para verlas todas abre `plantillas/catalogo.html`. Siempre con la fuente en pantalla, solo datos verificables, y como máximo una diapositiva de datos de cada cuatro.
9. **Variedad:** revisa que ningún título repita uno de las dos clases anteriores y que ninguna plantilla aparezca más de tres veces (salvo una serie).

## Después
10. El hook reconstruye `presentacion.html` y `contenido.md` y revisa el estilo en cada edición. Corrige cada advertencia.
11. Si agregaste o quitaste diapositivas, ajusta los tiempos de la escaleta y de los `<aside>` afectados para que la clase siga cabiendo en 50 minutos.
12. Pasa el estado de `clase.json` a `presentacion`.
13. Publica (o republica) `presentacion.html` como artefacto, según «Presentaciones como artefactos» en `CLAUDE.md`. Si es la primera vez, guarda el link en `artefacto` de `clase.json`. Si ya existía, usa ese mismo `url`.
14. Dale a Gio el link del artefacto y la ruta local de `presentacion.html`, con las teclas: F pantalla completa, P vista de presentador.
