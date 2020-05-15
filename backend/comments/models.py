from django.db import models
from biz.models import Biz
from core.models import User


class Comment(models.Model):
    content = models.TextField()
    biz = models.ForeignKey(Biz, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    reply = models.ForeignKey(
        "Comment", null=True, related_name="replies", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.comment
