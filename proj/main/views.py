from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Data


def index(request):
    return render(request, 'main/index.html')

def getData(request):
    return JsonResponse({
        'Data': [i.toDict() for i in Data.objects.all()]
        })

def getDataRender(request):
    datas = Data.objects.all()
    context = {
        'datas': datas,
    }
    return render(request, 'main/render.html', context)