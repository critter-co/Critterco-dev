from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        """Checks for "biz" field in comment PATCH, PUT and removes it if any is provided"""
        super().__init__(*args, **kwargs)
        if "view" in self.context and self.context["view"].action in [
            "update",
            "partial_update",
        ]:
            self.fields.pop("biz", None)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = (
            "id",
            "user",
            "created_at",
        )
