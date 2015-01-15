__author__ = 'zdvitas'
import httplib2

def check_session(request):
    c = httplib2.Http()
    req =  c.request("http://127.0.0.1:8080", method="POST", body="TEST")
    return False


def add_session(request):

    pass


def del_session(request):
    pass
