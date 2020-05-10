from rest_framework import serializers
from .models import Biz, Hours


class BizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biz
        fields = "__all__"
        read_only_fields = ["id", "created", "created_by"]


class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours
        fields = "__all__"
        read_only_fields = [
            "id",
        ]

