from django.contrib import admin
from .models import OrdenProduccion


@admin.register(OrdenProduccion)
class OrdenProduccionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "codigo",
        "producto",
        "receta",
        "cantidad_planificada",
        "cantidad_producida",
        "estado",
        "fecha_inicio",
        "fecha_fin",
        "activo",
    )
    list_filter = ("estado", "activo", "fecha_inicio", "fecha_fin")
    search_fields = ("codigo", "producto__codigo", "producto__nombre", "receta__nombre")