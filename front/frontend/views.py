# -*- coding: utf-8 -*-
# coding: utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
import httplib2
import os
import json

from sessions import *


def pc_back_url():
    return "http://127.0.0.1:8001"


def check_login(request):
    return {"name": "username", "id": 1}


def home(request):
    if check_session(request):
        return render(request, "main.html")
    else:
        return render(request, "auth.html")


def auth(request):
    if request.method == "POST":
        response = redirect("/")

        return response


def pc_one(request, id):
    '''
    Получаем инофрмацию об одном ПК и софту по нему
    '''
    context = {}
    con = httplib2.Http()
    head, resp = con.request(pc_back_url()+"/one?id="+str(id))
    context["pc"] = json.loads(resp)
    return render(request, "pc.html", context)

def pc_add(request):
    pc = {
        "name": os.urandom(3).encode('hex'),
        "params": os.urandom(4).encode('hex'),
        "count": 1,
        "owner": 1
    }
    con = httplib2.Http()
    head, resp = con.request(pc_back_url()+"/one", method="POST", body=json.dumps(pc))
    return redirect("/pc")


def pc_delete(request, id):
    con = httplib2.Http()
    head, resp = con.request(pc_back_url()+"/one?id="+str(id), method="DELETE")
    return redirect("/pc")


def pc_edit(request, id):
    con = httplib2.Http()
    head, resp = con.request(pc_back_url()+"/one?id="+str(id), body=json.dumps({"params": "edited!"}), method="PUT")
    return redirect("/pc")



def soft_delete(request, id):
    return None


def soft_edit(request, id):
    return None


def pc_list(request):
    '''
    Список всех ПК
    '''
    con = httplib2.Http()
    head, resp = con.request(pc_back_url())
    context = json.loads(resp)
    return render(request,"pc.html",context)