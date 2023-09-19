from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    
    def __str__(self):
        return self.title