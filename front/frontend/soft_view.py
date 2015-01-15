# -*- coding: utf-8 -*-
# coding: utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
import httplib2
import os
import json


def soft_back_url():
    return "http://127.0.0.1:8022"


def soft_one(request, id):
    '''

    '''
    context = {}
    con = httplib2.Http()
    head, resp = con.request(soft_back_url()+"/one?id="+str(id))
    context["pc"] = json.loads(resp)
    return render(request, "soft.html", context)


def soft_add(request):
    pc = {
        "name": os.urandom(3).encode('hex'),
        "producer": os.urandom(4).encode('hex'),
    }
    con = httplib2.Http()
    head, resp = con.request(soft_back_url()+"/one", method="POST", body=json.dumps(pc))
    return redirect("/pc")


def soft_list(request):
    '''
    Список всех ПК
    '''
    con = httplib2.Http()
    head, resp = con.request(soft_back_url())
    context = json.loads(resp)
    return render(request,"pc.html",context)


def soft_delete(request, id):
    con = httplib2.Http()
    head, resp = con.request(soft_back_url()+"/one?id="+str(id), method="DELETE")
    return redirect("/pc")


def soft_edit(request, id):
    con = httplib2.Http()
    head, resp = con.request(soft_back_url()+"/one?id="+str(id), body=json.dumps({"producer": "edited!"}), method="PUT")
    return redirect("/pc")
