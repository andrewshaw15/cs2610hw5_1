import datetime

from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    post_date = models.DateTimeField('Date Posted')

    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    content = models.TextField()
    post_date = models.DateTimeField('Date Posted')

    def __str__(self):
        return self.nickname