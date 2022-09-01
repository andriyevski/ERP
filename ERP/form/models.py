from django.db import models

# Create your models here.

class Client(models.Model):
    id_dep_client = models.TextField(max_length=100)
    name_client = models.TextField(max_length=100)

class Project_Num(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    id_dep_client = models.IntegerField()
    id_project = models.PositiveIntegerField()