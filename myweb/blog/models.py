from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    dmy = models.DateField()


