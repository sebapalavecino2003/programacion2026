from django.contrib import admin
from .models import CategoriaProducto, Producto


@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo',
        'nombre',
        'categoria',
        'precio_venta',
        'requiere_produccion',
        'activo',
    )
    list_filter = ('categoria', 'requiere_produccion', 'activo')
    search_fields = ('codigo', 'nombre')