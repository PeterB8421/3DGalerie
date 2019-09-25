from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Tato stránka nyní funguje")

def detail(request, model_id):
    return HttpResponse("Na této stránce bude výpis konkrétního objektu")

def create(request):
    return HttpResponse("Zde bude stránka pro vložení objektu do databáze")

def edit(request, model_id):
    return HttpResponse("Zde bude stránka pro editaci objektu")