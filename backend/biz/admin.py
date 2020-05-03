from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Biz


@admin.register(Biz)
class BizAdmin(OSMGeoAdmin):
    list_display = (
        "title",
        "location",
        "description",
        "address",
        "city",
        "phone",
        "gallery",
        "created",
    )
