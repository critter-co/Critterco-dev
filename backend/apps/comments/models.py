from django.db import models
from apps.biz.models import Biz
from apps.core.models import User


class Comment(models.Model):
    content = models.TextField()
    biz = models.ForeignKey(
        Biz, null=True, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    reply = models.ForeignKey(
        "Comment", null=True, related_name="replies", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
