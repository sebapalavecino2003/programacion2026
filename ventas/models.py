from django.db import models


class OrdenVenta(models.Model):
    ESTADO_CHOICES = [
        ("recibido", "Recibido"),
        ("en_revision", "En revision"),
        ("confirmado", "Confirmado"),
        ("rechazado", "Rechazado"),
    ]

    orden_produccion = models.OneToOneField(
        "produccion.OrdenProduccion",
        on_delete=models.PROTECT,
        related_name="orden_venta",
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="recibido",
    )
    observaciones = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    recibido_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Orden de venta"
        verbose_name_plural = "Ordenes de venta"
        ordering = ["-recibido_en"]

    def __str__(self):
        return f"Venta {self.orden_produccion.codigo}"

