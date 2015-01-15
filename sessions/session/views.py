from django.shortcuts import render
from django.shortcuts import HttpResponse
from session.models import *
import json
import os
# Create your views here.

def home(request):
    if request.method == "POST":
        ses = Session(session="fdsgfdsgds", user_id=21)
        ses.save()
        return HttpResponse(json.dumps({"status": "ok", "session": ses.session}))
    if request.method == "GET":
       pass
    if request.method == "DELETE":
        pass
    pass
