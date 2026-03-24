from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import OrdenVenta
from .serializers import OrdenVentaSerializer


class OrdenVentaViewSet(viewsets.ModelViewSet):
    queryset = OrdenVenta.objects.select_related(
        "orden_produccion",
        "orden_produccion__producto",
    ).all()
    serializer_class = OrdenVentaSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "orden_produccion__codigo",
        "orden_produccion__producto__nombre",
        "estado",
    ]
    ordering_fields = [
        "id",
        "estado",
        "recibido_en",
        "actualizado_en",
    ]
    ordering = ["-recibido_en"]

