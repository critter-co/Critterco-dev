from rest_framework import routers
from .views import CommentViewSet

router = routers.DefaultRouter()
router.register("api/comments", CommentViewSet, "comment")

urlpatterns = router.urls
