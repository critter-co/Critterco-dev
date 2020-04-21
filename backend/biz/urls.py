from rest_framework import routers
from .api import BizViewSet

router = routers.DefaultRouter()
router.register('api/biz', BizViewSet, 'biz')

urlpatterns = router.urls
