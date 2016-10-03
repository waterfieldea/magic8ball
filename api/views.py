from django.http import HttpResponse, HttpResponseBadRequest
from api.eightball import *
import json


def index(request):
    return HttpResponse("<h1>Index</h1>")


def answer(request):
    question = request.GET.get('question', None)
    if question is None:
        return HttpResponseBadRequest("Missing required question query parameter")
    else:
        eightball = EightBall()
        answer = eightball.ask_question(question)
        payload = json.dumps({"question": question, "answer": answer})
        return HttpResponse(payload)
