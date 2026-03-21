from django.db import models


class CategoriaMaterial(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Categoría de material"
        verbose_name_plural = "Categorías de materiales"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Material(models.Model):
    UNIDAD_CHOICES = [
        ("unidad", "Unidad"),
        ("kg", "Kilogramo"),
        ("g", "Gramo"),
        ("m", "Metro"),
        ("cm", "Centímetro"),
        ("litro", "Litro"),
        ("ml", "Mililitro"),
    ]

    codigo = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(
        CategoriaMaterial,
        on_delete=models.PROTECT,
        related_name="materiales"
    )
    unidad_medida = models.CharField(max_length=20, choices=UNIDAD_CHOICES, default="unidad")
    costo_referencia = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"