from django.db import models
from django.utils import timezone


class Video(models.Model):
    title = models.CharField(max_length=300)
    creator = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    category = models.CharField(max_length=300)
    upload_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='')

    def __str__(self):
        return self.title
