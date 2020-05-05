from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "name",
        "username",
        "is_active",
        "is_staff",
    )


admin.site.register(User, UsersAdmin)
