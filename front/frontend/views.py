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


def session_url():
    return "http://127.0.0.1:8080"

def check_login(request):
    return {"name": "username", "id": 1}


def home(request):

    if check_session(request):
        return redirect("/pc")
    else:
        return render(request, "auth.html")


def auth(request):
    if request.method == "POST":
        context = {}
        context["login"] = request.POST["login"]
        context["password"] = request.POST["password"]
        con = httplib2.Http()
        head, resp = con.request(session_url(), method="POST", body=json.dumps(context))
        resp = json.loads(resp)

        if resp["status"] == "ok":
            response = redirect("/pc")

            response.set_cookie("sessionid", resp["sessionid"])
            return response

        return render(request, "auth.html")





def soft_delete(request, id):
    return None


def soft_edit(request, id):
    return None


def logout(request):
    if not check_session(request):
        return redirect("/")
    context= {"sessionid" : request.COOKIES["sessionid"]}

    con = httplib2.Http()
    head, resp = con.request(session_url(), method="DELETE", body=json.dumps(context))
    resp = redirect("/")
    resp.delete_cookie("sessionid")
    return resp