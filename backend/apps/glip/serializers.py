from rest_framework import serializers

from apps.glip.models import Glip


class GlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glip
        fields = "__all__"
        read_only_fields = ["id", "uuid", "type", "date", "length"]
