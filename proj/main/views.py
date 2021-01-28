import json

from loguru import logger
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .models import Data


def index(request):
    return render(request, 'main/index.html')

def getData(request):
    return JsonResponse({
        'Data': [i.toDict() for i in Data.objects.all()]
        })

def getDataPk(request, pk):
    return JsonResponse({
        'Data': Data.objects.get(pk=pk).toDict()
        })

def getDataRender(request):
    datas = Data.objects.all()
    context = {
        'datas': datas,
    }
    return render(request, 'main/render.html', context)

def getDataVue(request):
    return render(request, 'main/vue.html')

@csrf_exempt
def sendNames(request):
    datas = Data.objects.all()
    return JsonResponse({
        'name': [data.Name for data in datas]
    }, safe=False)

    
@csrf_exempt
def sendAll(request):
    return JsonResponse({
        'Data': [i.toDict() for i in Data.objects.all()]
    }, safe=False)

@csrf_exempt
def namesFilter(request):
    params = json.loads(request.body.decode("utf-8"))
    textFilter = params['textFilter']
    filterCategory = params['filterCategory']

    logger.debug(textFilter)
    logger.debug(filterCategory)
    data = []

    if (filterCategory == "Категория"):
        logger.debug("Category!")
        data = Data.objects.filter(Category=textFilter)
    if (filterCategory == "Текст"):
        logger.debug("Text!")
        data = Data.objects.filter(Text=textFilter)
    if (filterCategory == "Имя"):
        logger.debug("Name!")
        data = Data.objects.filter(Name=textFilter)
    return JsonResponse({
        'Data': [i.toDict() for i in data],
        }, safe=False)