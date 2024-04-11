from datetime import datetime
from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    published_date = models.DateTimeField("date published", auto_now=True)
    created_date = models.DateTimeField("date created", auto_now_add=True)