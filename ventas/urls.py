from rest_framework.routers import DefaultRouter

from .views import OrdenVentaViewSet

router = DefaultRouter()
router.register(r"ordenes-venta", OrdenVentaViewSet, basename="orden-venta")

urlpatterns = router.urls

