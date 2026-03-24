from django.contrib import admin
from .models import Receta, RecetaDetalle


class RecetaDetalleInline(admin.TabularInline):
    model = RecetaDetalle
    extra = 1


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'nombre', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'producto__nombre', 'producto__codigo')
    inlines = [RecetaDetalleInline]


@admin.register(RecetaDetalle)
class RecetaDetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'receta', 'material', 'cantidad')
    search_fields = ('receta__producto__nombre', 'material__nombre')
