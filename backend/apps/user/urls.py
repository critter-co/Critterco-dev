from django.urls import path

from apps.user import views

app_name = "user"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("me", views.ManageUserView.as_view(), name="me"),
    path("confirm", views.ConfirmCodeView.as_view(), name="confirm"),
]
