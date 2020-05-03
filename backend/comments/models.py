from django.db import models


class Comment(models.Model):
    comment = models.TextField()
    favourite = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="user_favourite"
    )

    def __unicode__(self):
        return self.comment
