__author__ = 'zdvitas'
import httplib2
import json
def check_session(request):
    c = httplib2.Http()
    if "sessionid" in request.COOKIES:
        head , req =  c.request("http://127.0.0.1:8080", method="GET", body=json.dumps({"sessionid": request.COOKIES["sessionid"]}))
        req = json.loads(req)
        if req["status"] == "ok":
            return True
    return False


def add_session(request):

    pass


def del_session(request):
    pass
