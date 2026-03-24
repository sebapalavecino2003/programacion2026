from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Receta, RecetaDetalle
from .serializers import (
    RecetaSerializer,
    RecetaConDetallesSerializer,
    RecetaDetalleSerializer,
    RecetaDetalleCreateSerializer,
)


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.select_related('producto').prefetch_related('detalles__material').all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre', 'producto__nombre', 'producto__codigo']
    ordering_fields = ['id', 'nombre']
    ordering = ['nombre']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RecetaConDetallesSerializer
        return RecetaSerializer


class RecetaDetalleViewSet(viewsets.ModelViewSet):
    queryset = RecetaDetalle.objects.select_related('receta', 'receta__producto', 'material').all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['receta__producto__nombre', 'material__nombre', 'material__codigo']
    ordering_fields = ['id', 'cantidad']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RecetaDetalleSerializer
        return RecetaDetalleCreateSerializer
