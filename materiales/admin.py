from django.contrib import admin
from .models import CategoriaMaterial, Material


@admin.register(CategoriaMaterial)
class CategoriaMaterialAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "codigo",
        "nombre",
        "categoria",
        "unidad_medida",
        "costo_referencia",
        "activo",
    )
    list_filter = ("categoria", "unidad_medida", "activo")
    search_fields = ("codigo", "nombre")