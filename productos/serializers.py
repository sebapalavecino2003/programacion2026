from rest_framework import serializers
from .models import CategoriaProducto, Producto


class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ['id', 'nombre', 'descripcion']


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id',
            'codigo',
            'nombre',
            'descripcion',
            'categoria',
            'categoria_nombre',
            'precio_venta',
            'requiere_produccion',
            'activo',
            'creado_en',
            'actualizado_en',
        ]