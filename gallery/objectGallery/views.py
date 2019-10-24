from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ObjectModel
from .forms import ObjectModelForm


#Stránka pro listr modelů
def index(request):
    objectList = ObjectModel.objects.all() #Získání listu z db
    context = {'models': objectList} #Předání proměnné do templatu
    #messages.info(request, "Hello world")
    return render(request, 'objectGallery/index.html', context) #Vyrenderování stránky

#Stránka pro zobrazení modelu s three.js a pro zobrazení detailů modelu
def detail(request, model_id):
    model = get_object_or_404(ObjectModel, pk=model_id)
    context = {"model": model}
    return render(request, "objectGallery/detail.html", context=context)

#Stránka pro vytvoření modelu
@login_required(login_url="/log/in")
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
@login_required(login_url="/log/in")
def edit(request, model_id):
    model = get_object_or_404(ObjectModel, pk=model_id) #Získání modelu z databáze
    form = ObjectModelForm(request.POST or None, request.FILES or None, instance=model) #Vytvoření instance formuláře
    if form.is_valid():
        form.save() #Uložení formuláře a updatování dat
        messages.success(request, "Model úspěšné upraven") #Zpráva o úspěchu
        return HttpResponseRedirect(reverse("index")) #Přesměrování na index
    return render(request, "objectGallery/edit.html", {"form": form}) #Jinak se vyrenderuje stránka s formulářem

#Metoda pro vymazání modelu z databáze podle id
@login_required(login_url="/log/in")
def delete(request, model_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Nemáte oprávnění smazat model!")
        return HttpResponseRedirect(reverse("index"))
    else:
        model = ObjectModel.objects.get(pk=model_id)
        if model is not None: #Jestli model existuje, tak se smaže, jinak se vypíše chybová hláška
            model.delete() #Vymazání modelu
            messages.success(request, "Model vymazán z databáze") #Zpráva o úspěchu
            return HttpResponseRedirect(reverse("index")) #Přesměrování na index
        else:
            messages.warning(request, "Model nebyl nalezen")
            return HttpResponseRedirect(reverse("index"))

def user_login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.info(request, "Byli jste úspěšně přihlášeni, vítejte %s" % user.get_username())
        if request.GET.get("next", False):
            return HttpResponseRedirect(request.GET.get("next"))
        else:
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "objectGallery/log_in.html")

def user_logout(request):
    logout(request)
    messages.info(request, "Byli jste odhlášeni")
    return HttpResponseRedirect(reverse("index"))