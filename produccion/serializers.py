from rest_framework import serializers
from .models import OrdenProduccion


class OrdenProduccionSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source="producto.nombre", read_only=True)
    producto_codigo = serializers.CharField(source="producto.codigo", read_only=True)
    receta_nombre = serializers.CharField(source="receta.nombre", read_only=True)
    estado_display = serializers.CharField(source="get_estado_display", read_only=True)

    class Meta:
        model = OrdenProduccion
        fields = [
            "id",
            "codigo",
            "producto",
            "producto_codigo",
            "producto_nombre",
            "receta",
            "receta_nombre",
            "cantidad_planificada",
            "cantidad_producida",
            "estado",
            "estado_display",
            "fecha_inicio",
            "fecha_fin",
            "observaciones",
            "activo",
            "creado_en",
            "actualizado_en",
        ]
        read_only_fields = ["creado_en", "actualizado_en"]

    def validate_producto(self, value):
        if not value.requiere_produccion:
            raise serializers.ValidationError(
                "Solo se pueden crear órdenes para productos que requieren producción."
            )
        return value

    def validate_cantidad_planificada(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "La cantidad planificada debe ser mayor a cero."
            )
        return value

    def validate_cantidad_producida(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "La cantidad producida no puede ser negativa."
            )
        return value

    def validate(self, attrs):
        producto = attrs.get("producto", getattr(self.instance, "producto", None))
        receta = attrs.get("receta", getattr(self.instance, "receta", None))
        cantidad_planificada = attrs.get(
            "cantidad_planificada",
            getattr(self.instance, "cantidad_planificada", None)
        )
        cantidad_producida = attrs.get(
            "cantidad_producida",
            getattr(self.instance, "cantidad_producida", 0)
        )
        fecha_inicio = attrs.get("fecha_inicio", getattr(self.instance, "fecha_inicio", None))
        fecha_fin = attrs.get("fecha_fin", getattr(self.instance, "fecha_fin", None))
        estado = attrs.get("estado", getattr(self.instance, "estado", None))

        if producto and receta and receta.producto_id != producto.id:
            raise serializers.ValidationError({
                "receta": "La receta seleccionada no corresponde al producto indicado."
            })

        if cantidad_planificada is not None and cantidad_producida is not None:
            if cantidad_producida > cantidad_planificada:
                raise serializers.ValidationError({
                    "cantidad_producida": "La cantidad producida no puede ser mayor a la planificada."
                })

        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            raise serializers.ValidationError({
                "fecha_fin": "La fecha de fin no puede ser anterior a la fecha de inicio."
            })

        if estado == "terminado" and cantidad_planificada is not None and cantidad_producida != cantidad_planificada:
            raise serializers.ValidationError({
                "estado": "Para marcar como terminado, la cantidad producida debe ser igual a la planificada."
            })

        return attrs