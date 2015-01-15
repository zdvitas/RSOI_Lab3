from django.db import models

# Create your models here.


class Session(models.Model):
    session = models.CharField(max_length=40)
    user_id = models.IntegerField()