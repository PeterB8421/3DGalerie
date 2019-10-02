from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import ObjectModel
from objectGallery.forms import ModelForm

def index(request):
    objectList = get_list_or_404(ObjectModel)
    context = {'models': objectList}
    return render(request, 'objectGallery/index.html', context)

def detail(request, model_id):
    return HttpResponse("Na této stránce bude výpis konkrétního objektu")

def create(request):
    return HttpResponse("Zde bude stránka pro vložení objektu do databáze")

def edit(request, model_id):
    return HttpResponse("Zde bude stránka pro editaci objektu")