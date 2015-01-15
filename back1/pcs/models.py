# -*- coding: utf-8 -*-
# coding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime
import json



class Computer(models.Model):
    owner = models.IntegerField()
    count = models.IntegerField()
    name = models.CharField(max_length=100)
    params = models.CharField(max_length=200)
    # programs = models.ManyToManyField(Program)

    def to_dic(self):
        dic = {
            "id": self.id,
            "name": self.name,
            "count": self.count,
            "params": self.params,
            "owner": self.owner
        }
        return dic
