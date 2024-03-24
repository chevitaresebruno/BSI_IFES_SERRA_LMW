from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def add(self):
        self.save()
        
    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(blank=True, null=True)

    def publish(self, created_date):
        self.created_date = created_date
        self.last_update = created_date
        self.save()
    
    def update(self, text, update_date):
        self.text = text
        self.last_update = update_date
        self.save()

    def __str__(self):
        return self.title