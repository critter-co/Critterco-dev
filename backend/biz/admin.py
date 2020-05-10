from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Biz, Hours


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
        "website",
        "instagram",
    )


@admin.register(Hours)
class HoursAdmin(OSMGeoAdmin):
    list_display = ("id", "weekday", "to_hour")
