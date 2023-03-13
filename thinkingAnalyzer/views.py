import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import thinkingFunction, thinkingFunctionDetail

def index(request):
    TF = list(thinkingFunction.objects.all().values())
    TFD = list(thinkingFunctionDetail.objects.all().values())

    jsonTF = {
        'thinkingFunction' : TF,
        'thinkingFunctionDetail' : TFD,
    }

    response = JsonResponse(jsonTF)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
