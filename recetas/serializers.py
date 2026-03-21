from rest_framework import serializers
from .models import Receta, RecetaDetalle


class RecetaDetalleSerializer(serializers.ModelSerializer):
    material_nombre = serializers.CharField(source='material.nombre', read_only=True)
    material_codigo = serializers.CharField(source='material.codigo', read_only=True)
    unidad_medida = serializers.CharField(source='material.unidad_medida', read_only=True)
    unidad_medida_display = serializers.CharField(source='material.get_unidad_medida_display', read_only=True)

    class Meta:
        model = RecetaDetalle
        fields = [
            'id',
            'material',
            'material_codigo',
            'material_nombre',
            'unidad_medida',
            'unidad_medida_display',
            'cantidad',
            'observaciones',
        ]


class RecetaDetalleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaDetalle
        fields = [
            'id',
            'receta',
            'material',
            'cantidad',
            'observaciones',
        ]

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor a cero.")
        return value


class RecetaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_codigo = serializers.CharField(source='producto.codigo', read_only=True)

    class Meta:
        model = Receta
        fields = [
            'id',
            'producto',
            'producto_codigo',
            'producto_nombre',
            'nombre',
            'descripcion',
            'activo',
            'creado_en',
            'actualizado_en',
        ]
        read_only_fields = ['creado_en', 'actualizado_en']

    def validate_producto(self, value):
        if not value.requiere_produccion:
            raise serializers.ValidationError(
                "Solo se puede crear una receta para productos que requieren producción."
            )
        return value


class RecetaConDetallesSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_codigo = serializers.CharField(source='producto.codigo', read_only=True)
    detalles = RecetaDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Receta
        fields = [
            'id',
            'producto',
            'producto_codigo',
            'producto_nombre',
            'nombre',
            'descripcion',
            'activo',
            'creado_en',
            'actualizado_en',
            'detalles',
        ]