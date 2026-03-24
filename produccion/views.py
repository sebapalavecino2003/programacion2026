from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import OrdenProduccion
from .serializers import OrdenProduccionSerializer


class OrdenProduccionViewSet(viewsets.ModelViewSet):
    queryset = OrdenProduccion.objects.select_related("producto", "receta").all()
    serializer_class = OrdenProduccionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "codigo",
        "producto__codigo",
        "producto__nombre",
        "receta__nombre",
        "estado",
    ]
    ordering_fields = [
        "id",
        "codigo",
        "estado",
        "fecha_inicio",
        "fecha_fin",
    ]
    ordering = ["-id"]
