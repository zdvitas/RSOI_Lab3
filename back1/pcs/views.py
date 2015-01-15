from django.shortcuts import render
from django.shortcuts import HttpResponse
from pcs.models import *
import json
# Create your views here.


def pc_list(request):
    pc_set = Computer.objects.all()
    dictionaries = [obj.to_dic() for obj in pc_set]
    return HttpResponse(json.dumps({"data": dictionaries}))


def one(request):

    if request.method == "POST":  # Add new
        dic = json.loads(request.body)
        pc = Computer(name=dic["name"], owner=dic["owner"], params=dic["params"], count=dic["count"])
        pc.save()
        return HttpResponse(json.dumps({"status": "ok"}))
    try:
        id = int(request.GET["id"])
        pc = Computer.objects.all().filter(id=id)
        if len(pc) == 0:
            raise Exception("Invalid id")
        pc = pc[0]
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(e)}))

    if request.method == "GET":
        resp = json.dumps(pc.to_dic())
        return HttpResponse(resp)

    if request.method == "DELETE":
        pc.delete()
        return HttpResponse(json.dumps({"status": "ok"}))

    if request.method == "PUT":  # Edit
        edited = json.loads(request.body)
        pc.params = edited["params"]
        pc.save()
        return HttpResponse(json.dumps({"status": "ok"}))
