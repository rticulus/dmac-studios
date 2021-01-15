from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class POST(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
