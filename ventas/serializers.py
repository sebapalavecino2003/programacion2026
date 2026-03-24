from rest_framework import serializers

from .models import OrdenVenta


class OrdenVentaSerializer(serializers.ModelSerializer):
    orden_codigo = serializers.CharField(
        source="orden_produccion.codigo",
        read_only=True,
    )
    producto_nombre = serializers.CharField(
        source="orden_produccion.producto.nombre",
        read_only=True,
    )
    cantidad_planificada = serializers.DecimalField(
        source="orden_produccion.cantidad_planificada",
        max_digits=12,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = OrdenVenta
        fields = [
            "id",
            "orden_produccion",
            "orden_codigo",
            "producto_nombre",
            "cantidad_planificada",
            "estado",
            "observaciones",
            "activo",
            "recibido_en",
            "actualizado_en",
        ]
        read_only_fields = ["recibido_en", "actualizado_en"]

    def validate_orden_produccion(self, value):
        if value.estado != "terminado":
            raise serializers.ValidationError(
                "Solo se puede enviar a ventas una orden de produccion terminada."
            )
        return value

