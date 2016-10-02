from django.http import HttpResponse, HttpResponseBadRequest
from api.eightball import *


def index(request):
    return HttpResponse("<h1>Index</h1>")


def answer(request):
    question = request.GET.get('question', None)
    if question is None:
        return HttpResponseBadRequest("Missing required question query parameter")
    else:
        eightball = EightBall()
        return HttpResponse("<h1>{0}</h1>".format(eightball.ask_question(question)))
