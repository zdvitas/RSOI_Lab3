from django.shortcuts import render
from django.shortcuts import HttpResponse
from session.models import *
import os
import json
import os
# Create your views here.


def home(request):
    if request.method == "POST":
        dic = json.loads(request.body)
        user = Person.objects.all().filter(login=dic["login"], password=dic["password"])
        if len(user) == 0:
            return HttpResponse(json.dumps({"status": "fail"}))

        user = user[0]
        ses = Session.objects.all().filter(user_id=user.id)
        for s in ses:
            s.delete()
        ses = Session(session=os.urandom(6).encode('hex'), user_id=user.id)
        ses.save()
        return HttpResponse(json.dumps({"status": "ok", "sessionid": ses.session}))

    if request.method == "GET":
        dic = json.loads(request.body)
        ses = Session.objects.all().filter(session=dic["sessionid"])
        if len(ses) == 0:
            return HttpResponse(json.dumps({"status": "fail"}))
        return HttpResponse(json.dumps({"status": "ok"}))

    if request.method == "DELETE":
        dic = json.loads(request.body)
        ses = Session.objects.all().filter(session=dic["sessionid"])
        for s in ses:
            s.delete()
        return HttpResponse(json.dumps({"status": "ok"}))
    pass
