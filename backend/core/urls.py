from rest_framework import routers
from .api import BizViewSet, HoursViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register("api/biz", BizViewSet, "biz")
router.register("api/hours", HoursViewSet, "hours")
router.register("api/comments", CommentViewSet, "comment")

urlpatterns = router.urls
