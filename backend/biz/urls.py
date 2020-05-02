from rest_framework import routers
from .api import BizViewSet, HoursViewSet

router = routers.DefaultRouter()
router.register("api/biz", BizViewSet, "biz")
router.register("api/hours", HoursViewSet, "hours")

urlpatterns = router.urls
