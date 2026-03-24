from rest_framework import serializers
from .models import Proveedor


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            "id",
            "codigo",
            "nombre",
            "documento",
            "email",
            "telefono",
            "direccion",
            "ciudad",
            "activo",
        ]
