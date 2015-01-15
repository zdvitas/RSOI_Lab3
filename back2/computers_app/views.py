from django.shortcuts import render
from django.shortcuts import HttpResponse
from computers_app.models import *
import json
# Create your views here.


def soft_list(request):
    pc_id = int(request.GET["id"])
    pc_set = Connect.objects.all().filter(pc_id=pc_id)
    soft_set = []
    for pc in pc_set:
        soft_set.append(Program.objects.all().filter(id=pc.id))
    dictionaries = [obj[0].to_dic() for obj in soft_set]
    return HttpResponse(json.dumps({"data": dictionaries}))


def one(request):

    if request.method == "POST":  # Add new
        dic = json.loads(request.body)
        soft = Program(name=dic["name"],  producer=dic["producer"], )
        soft.save()
        return HttpResponse(json.dumps({"status": "ok"}))
    try:
        id = int(request.GET["id"])
        soft = Program.objects.all().filter(id=id)
        if len(soft) == 0:
            raise Exception("Invalid id")
        soft = soft[0]
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(e)}))

    if request.method == "GET":
        resp = json.dumps(soft.to_dic())
        return HttpResponse(resp)

    if request.method == "DELETE":
        cons = Connect.objects.all().filter(soft_id=soft.id)
        for obj in cons:
            obj.delete()
        soft.delete()

        return HttpResponse(json.dumps({"status": "ok"}))

    if request.method == "PUT":  # Edit
        edited = json.loads(request.body)
        soft.producer = edited["producer"]
        soft.save()
        return HttpResponse(json.dumps({"status": "ok"}))
