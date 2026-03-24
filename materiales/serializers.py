from rest_framework import serializers
from .models import CategoriaMaterial, Material


class CategoriaMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMaterial
        fields = ["id", "nombre"]


class MaterialSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source="categoria.nombre", read_only=True)
    unidad_medida_display = serializers.CharField(source="get_unidad_medida_display", read_only=True)

    class Meta:
        model = Material
        fields = [
            "id",
            "codigo",
            "nombre",
            "categoria",
            "categoria_nombre",
            "unidad_medida",
            "unidad_medida_display",
            "costo_referencia",
            "activo",
        ]
