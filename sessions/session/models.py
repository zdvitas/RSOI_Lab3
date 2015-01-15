from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Session(models.Model):
    session = models.CharField(max_length=40)
    user_id = models.IntegerField()