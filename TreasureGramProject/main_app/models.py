# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.name, self.value)