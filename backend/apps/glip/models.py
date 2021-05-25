from django.db import models
import uuid

class Glip(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    length = models.CharField(max_length=50)
    tags = models.CharField(max_length=255)
    thumbnail = models.ImageField(default='', blank=True)
