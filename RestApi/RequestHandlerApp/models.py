# from django.db import models
# from django.contrib.mongodb.fields import ArrayField
# from mongoengine import *
# from mongoengine import Document, EmbeddedDocument, fields
from djongo import models

class aimapsModel(models.Model):
    _id = models.CharField(max_length=255)
    canEdit = models.JSONField()
    canView = models.JSONField()
    item = models.CharField(max_length=255)
    siteid = models.CharField(max_length=255)
    data = models.JSONField()
    maps = models.JSONField()
    image = models.CharField(max_length=255)
    creatorid = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=False)
    updatedA = models.DateTimeField(auto_now_add=False)
    route = models.JSONField()
    bulkdata = models.JSONField(null=True, blank=True)
    class Meta:
        db_table = 'aimaps'


class demoModels(models.Model):
    name = models.CharField(max_length=100)
    collections = models.JSONField()

class demo2Model(models.Model):
    name = models.CharField(max_length=100)
    collections = models.JSONField()
class NewModel(models.Model):
    name = models.CharField(max_length=100)
    collections = models.JSONField()
class final_model(models.Model):
    name = models.CharField(max_length=100)
    collections = models.JSONField()
