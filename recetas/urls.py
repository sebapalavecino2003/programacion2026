from rest_framework.routers import DefaultRouter
from .views import RecetaViewSet, RecetaDetalleViewSet

router = DefaultRouter()
router.register(r'recetas', RecetaViewSet, basename='receta')
router.register(r'recetas-detalles', RecetaDetalleViewSet, basename='receta-detalle')

urlpatterns = router.urls