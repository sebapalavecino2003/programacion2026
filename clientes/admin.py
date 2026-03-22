from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "codigo",
        "nombre",
        "tipo_cliente",
        "documento",
        "telefono",
        "ciudad",
        "activo",
    )
    list_filter = ("tipo_cliente", "activo", "ciudad")
    search_fields = ("codigo", "nombre", "documento", "email", "telefono")