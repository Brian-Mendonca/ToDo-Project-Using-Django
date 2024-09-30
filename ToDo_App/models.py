from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='[No Description]')
    completed = models.BooleanField(default=False)