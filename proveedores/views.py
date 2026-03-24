from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Proveedor
from .serializers import ProveedorSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "codigo",
        "nombre",
        "documento",
        "email",
        "telefono",
        "ciudad",
    ]
    ordering_fields = [
        "id",
        "codigo",
        "nombre",
        "ciudad",
    ]
    ordering = ["nombre"]
