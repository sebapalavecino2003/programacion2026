from rest_framework.routers import DefaultRouter
from .views import OrdenProduccionViewSet

router = DefaultRouter()
router.register(r'ordenes-produccion', OrdenProduccionViewSet, basename='orden-produccion')

urlpatterns = router.urls