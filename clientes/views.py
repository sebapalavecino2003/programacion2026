from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
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
        "tipo_cliente",
        "ciudad",
    ]
    ordering = ["nombre"]
