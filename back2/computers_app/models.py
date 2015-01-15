from django.db import models

# Create your models here.

class Program(models.Model):
    name = models.CharField(max_length=20)
    producer = models.CharField(max_length=20)

    def to_dic(self):
        dic = {
            "id": self.id,
            "name": self.name,
            "producer": self.producer
        }
        return dic

class Connect(models.Model):
    pc_id = models.IntegerField()
    soft_id = models.IntegerField()