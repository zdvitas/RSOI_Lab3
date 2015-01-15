from django.shortcuts import render
from django.shortcuts import HttpResponse
from pcs.models import *
# Create your views here.


def pc_list(request):
    pc_set = Computer.objects.all()
    dictionaries = [obj.to_dic() for obj in pc_set]
    return HttpResponse(json.dumps({"data": dictionaries}))


def one(request):
    if request.method == "GET":
        pass
    if request.method == "DELETE":
        pass
    if request.method == "POST":  # Add new
        pass
    if request.method == "PUT": # Edit
        pass
