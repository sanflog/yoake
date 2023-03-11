from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import thinkingFunction

def index(request):
    f = thinkingFunction.objects.all()
    fn = f[0]
    obj = {
        'title' : fn.title,
        'target' : fn.target,
        'function' : fn.function,
        'fType' : fn.fType,
        'time' : fn.time,
        'decideTo' : fn.decideTo
    }
    return JsonResponse(obj)
