from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    tipo_cliente_display = serializers.CharField(
        source="get_tipo_cliente_display",
        read_only=True
    )

    class Meta:
        model = Cliente
        fields = [
            "id",
            "codigo",
            "nombre",
            "tipo_cliente",
            "tipo_cliente_display",
            "documento",
            "email",
            "telefono",
            "direccion",
            "ciudad",
            "observaciones",
            "activo",
            "creado_en",
            "actualizado_en",
        ]
        read_only_fields = ["creado_en", "actualizado_en"]