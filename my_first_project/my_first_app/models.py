from django.db import models

# Create your models here.
class Cuchao(models.Model):
    title = models.TextField(max_length=255)
