from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UrlData(models.Model):
    url = models.URLField(max_length=200)
    slug = models.CharField(max_length=30, unique=True)
    
    def __str__(self) -> str:
        return f"Short Url for: {self.url} is {self.slug}"
