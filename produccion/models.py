from django.db import models


class OrdenProduccion(models.Model):
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("en_proceso", "En proceso"),
        ("terminado", "Terminado"),
        ("cancelado", "Cancelado"),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    producto = models.ForeignKey(
        "productos.Producto",
        on_delete=models.PROTECT,
        related_name="ordenes_produccion"
    )
    receta = models.ForeignKey(
        "recetas.Receta",
        on_delete=models.PROTECT,
        related_name="ordenes_produccion"
    )
    cantidad_planificada = models.DecimalField(max_digits=12, decimal_places=2)
    cantidad_producida = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="pendiente"
    )
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Orden de producción"
        verbose_name_plural = "Órdenes de producción"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.codigo} - {self.producto.nombre}"
