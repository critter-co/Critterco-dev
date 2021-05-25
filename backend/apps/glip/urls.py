from rest_framework import routers

from .views import GlipViewSet

router = routers.DefaultRouter()
router.register("api/glip", GlipViewSet, "glip")

urlpatterns = router.urls