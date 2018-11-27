from django.db import models

# Create your models here.
class content(models.Model):
    name = models.CharField(max_length=20)
    original = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

class comment(models.Model):
    content = models.CharField(max_length=255)
    time = models.DateTimeField()
