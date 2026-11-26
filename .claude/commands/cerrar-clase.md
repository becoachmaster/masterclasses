---
description: Cierra una clase dictada y actualiza la base de conocimiento (Fase 6)
argument-hint: [número de clase] [cómo fue la clase, opcional]
---
Datos: $ARGUMENTS (si no hay número, la última clase no cerrada).

1. Completa en `clase.json`, a partir de la escaleta, las diapositivas y lo que cuente Gio:
   - `fecha` (real, si Gio la da), `aprendizajes` (exactamente 3, frases cortas en lenguaje de la audiencia), `repaso` (los mismos 3 en versión de pantalla, de 8 palabras o menos: es lo que muestra `@repaso` en la clase siguiente), `frase_ancla`, `compromiso`, `bucle_abierto`.
   - `temas`, `herramientas`, `ejercicio`, `terminos` (cada uno con `termino` y `definicion`), `fuentes`.
   - `observaciones_post_clase` con lo que Gio cuente (qué funcionó, qué no, participación).
   - Agrega un evento en `historial` y pasa `estado` a `cerrada`.
2. Escribe `notas-publicas.md` con la plantilla `plantillas/notas-publicas.md`. Es para la comunidad y el futuro sitio web: sin notas internas ni tiempos.
3. Si en esta clase surgieron correcciones generales, regístralas en `conocimiento/reglas-aprendidas.md`; decisiones del programa en `conocimiento/decisiones.md`; ideas de temas en `conocimiento/ideas-temas.md`.
4. El hook regenera la bitácora, el mapa de temas y el glosario, y reconstruye la presentación de la siguiente clase (su repaso depende de esta). Verifica que no haya advertencias. Si el hook avisa que un artefacto quedó desactualizado, republícalo con su `url`.
5. Si el proyecto es un repositorio git, haz un commit: `Clase NNN cerrada: <título>`.
