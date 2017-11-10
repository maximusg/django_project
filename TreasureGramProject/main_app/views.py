# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from main_app.models import Treasure
#from django.http import HttpResponse

#adding index page
def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})
# Create your views here.

"""class Treasure: 
    def __init__(self, name, value, material, location, img):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img = img
        """


