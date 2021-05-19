from rest_framework import routers
from .views import BizViewSet, HoursViewSet

router = routers.DefaultRouter()
router.register("api/biz", BizViewSet, "biz")
router.register("api/hours", HoursViewSet, "hours")

urlpatterns = router.urls
