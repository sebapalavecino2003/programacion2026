from django.db import models


class Receta(models.Model):
    producto = models.OneToOneField(
        'productos.Producto',
        on_delete=models.PROTECT,
        related_name='receta'
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
        ordering = ["nombre"]

    def __str__(self):
        return f"Receta de {self.producto.nombre}"


class RecetaDetalle(models.Model):
    receta = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    material = models.ForeignKey(
        'materiales.Material',
        on_delete=models.PROTECT,
        related_name='recetas_detalle'
    )
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = "Detalle de receta"
        verbose_name_plural = "Detalles de receta"
        ordering = ["id"]
        unique_together = ("receta", "material")

    def __str__(self):
        return f"{self.receta.producto.nombre} - {self.material.nombre} ({self.cantidad})"
