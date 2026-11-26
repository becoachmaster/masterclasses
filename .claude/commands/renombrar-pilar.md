---
description: Cambia el nombre de un pilar (por ejemplo, el tercero, que es provisional)
argument-hint: <id del pilar> <nuevo nombre>
---
Cambio pedido: $ARGUMENTS

1. Edita solo `conocimiento/pilares.json`: cambia `nombre` (y `descripcion` si hace falta). No cambies el `id`. Si el nombre queda definitivo, pon `provisional` en `false`.
2. Busca el nombre anterior escrito a mano en `conocimiento/*.md` (excepto los archivos generados) y en diapositivas de clases no cerradas, y actualízalo.
3. Registra la decisión en `conocimiento/decisiones.md` con la fecha.
4. El hook reconstruye todas las presentaciones. Confirma que no haya advertencias.
