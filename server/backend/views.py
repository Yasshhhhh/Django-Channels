from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def hello(req):
    return JsonResponse("HELLO World",safe=False)
    