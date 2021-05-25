from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from backend.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.biz.urls")),
    path("", include("apps.glip.urls")),
    path("", include("apps.comments.urls")),
    path('api/graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    path("api/user/", include("apps.user.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    url(
        r"^api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [url(r"^api/silk/", include("silk.urls", namespace="silk"))]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)), ] + urlpatterns
