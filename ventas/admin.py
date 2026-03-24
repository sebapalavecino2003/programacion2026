from django.contrib import admin

from .models import OrdenVenta


@admin.register(OrdenVenta)
class OrdenVentaAdmin(admin.ModelAdmin):
    list_display = ("id", "orden_produccion", "estado", "activo", "recibido_en")
    search_fields = (
        "orden_produccion__codigo",
        "orden_produccion__producto__nombre",
        "estado",
    )
    list_filter = ("estado", "activo", "recibido_en")

