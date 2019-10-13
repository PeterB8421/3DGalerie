from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.urls import reverse
from .models import ObjectModel
from .forms import ObjectModelForm
from objectGallery.forms import ObjectModelForm


#Stránka pro listr modelů
def index(request):
    objectList = get_list_or_404(ObjectModel) #Získání listu z db
    context = {'models': objectList} #Předání proměnné do templatu
    #messages.info(request, "Hello world")
    return render(request, 'objectGallery/index.html', context) #Vyrenderování stránky

#Stránka pro zobrazení modelu s three.js a pro zobrazení detailů modelu
def detail(request, model_id):
    model = get_object_or_404(ObjectModel, pk=model_id)
    context = {"model": model}
    return render(request, "objectGallery/detail.html", context=context)

#Stránka pro vytvoření modelu
def create(request):
    if request.method == "POST": #Jestli byl formulář odeslán, metoda bude POST
        form = ObjectModelForm(request.POST, request.FILES) #Předání dat pro uložení
        if form.is_valid():
            form.save() #Uložení formuláře
            messages.success(request, "Objekt úspěšně přidán do databáze") #Zobrazení zprávy o úspěšném uložení
            return HttpResponseRedirect(reverse("index")) #Přesměrování na stránku index

    else:
        form = ObjectModelForm() #Při prvním požadavku se inicializuje formulář
    return render(request, "objectGallery/create.html", {"form": form}) #Vyrenderování stránky s formulářem

#Stránka pro editaci modelu
def edit(request, model_id):
    model = get_object_or_404(ObjectModel, pk=model_id) #Získání modelu z databáze
    form = ObjectModelForm(request.POST or None, request.FILES or None, instance=model) #Vytvoření instance formuláře
    if form.is_valid():
        form.save() #Uložení formuláře a updatování dat
        messages.success(request, "Model úspěšné upraven") #Zpráva o úspěchu
        return HttpResponseRedirect(reverse("index")) #Přesměrování na index
    return render(request, "objectGallery/edit.html", {"form": form}) #Jinak se vyrenderuje stránka s formulářem

#Metoda pro vymazání modelu z databáze podle id
def delete(request, model_id):
    model = get_object_or_404(ObjectModel, pk=model_id) #Získání požadovaného modelu
    model.delete() #Vymazání modelu
    messages.success(request, "Model vymazán z databáze") #Zpráva o úspěchu
    return HttpResponseRedirect(reverse("index")) #Přesměrování na index