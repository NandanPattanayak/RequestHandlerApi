from django.db import models

# Create your models here.
class demoModels(models.Model):
    name = models.CharField(max_length=100)
    collections = models.JSONField()

class demo2Model(models.Model):
    name = models.CharField(max_length=100)
    collections = models.JSONField()
