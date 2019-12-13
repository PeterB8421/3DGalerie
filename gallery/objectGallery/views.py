from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ObjectModel, Files, Tags
from .forms import ObjectModelForm, FilesModelForm, TagsModelForm


# Stránka pro listr modelů
def index(request):
    objectList = ObjectModel.objects.all() # Získání listu z db
    context = {'models': objectList} # Předání proměnné do templatu
    # messages.info(request, "Hello world")
    return render(request, 'objectGallery/index.html', context) # Vyrenderování stránky

# Stránka pro zobrazení modelu s three.js a pro zobrazení detailů modelu
def detail(request, model_id):
    model = get_object_or_404(ObjectModel, pk=model_id)
    images = Files.objects.filter(model_id=model_id)
    tags = Tags.objects.filter(model_ids=model_id)
    context = {"model": model, "imgs": images, "tags": tags}
    return render(request, "objectGallery/detail.html", context=context)

# Stránka pro vytvoření modelu
@login_required(login_url="/log/in")
def create(request):
    if request.method == "POST": # Jestli byl formulář odeslán, metoda bude POST
        form = ObjectModelForm(request.POST, request.FILES) # Předání dat pro uložení   
        if form.is_valid():
            saved_form = form.save() # Uložení formuláře
            messages.success(request, "Objekt úspěšně přidán do databáze") # Zobrazení zprávy o úspěšném uložení
            return HttpResponseRedirect(reverse("edit", kwargs={"model_id": saved_form.pk})) # Přesměrování na stránku index

    else:
        form = ObjectModelForm() # Při prvním požadavku se inicializuje formulář
    return render(request, "objectGallery/create.html", {"form": form}) # Vyrenderování stránky s formulářem

# Stránka pro přidání galerie obrázků k modelu
@login_required(login_url="/log/in")
def addGallery(request, model_id):
    if request.method == "POST":
        form = FilesModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            if request.FILES:
                id_model = ObjectModel.objects.only("id").get(id=model_id)
                for f in request.FILES.getlist("f"):
                    Files.objects.create(model_id=id_model, f=f)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = FilesModelForm()
        context = {"form": form, "model_id": model_id}
        return render(request, "objectGallery/addGallery.html", context=context)

# Stránka pro editaci modelu
@login_required(login_url="/log/in")
def edit(request, model_id):
    model = get_object_or_404(ObjectModel, pk=model_id) # Získání modelu z databáze
    form = ObjectModelForm(request.POST or None, request.FILES or None, instance=model) # Vytvoření instance formuláře
    imgs = Files.objects.filter(model_id=model_id)
    galleryForm = FilesModelForm(request.POST or None, request.FILES or None)
    tagsForm = TagsModelForm
    tags = list(Tags.objects.filter(model_ids=model_id).values())
    context = {
        "form": form,
        "imgs": imgs,
        "galleryForm": galleryForm,
        "tagsForm": tagsForm,
        "model": model,
        "tags": tags
    }
    if form.is_valid() and galleryForm.is_valid():
        form.save() # Uložení formuláře a updatování dat
        galleryForm.save(commit=False)
        if request.FILES:
            id_model = ObjectModel.objects.only("id").get(id=model_id)
            for f in request.FILES.getlist("f"):
                Files.objects.create(model_id=id_model, f=f)
        messages.success(request, "Model úspěšné upraven") # Zpráva o úspěchu
        return HttpResponseRedirect(reverse("index")) # Přesměrování na index
    return render(request, "objectGallery/edit.html", context) # Jinak se vyrenderuje stránka s formulářem

@login_required(login_url="/log/in")
def ajaxAddTag(request, model_id, tag):
    id_model = ObjectModel.objects.only("id").get(id=model_id)
    tag = Tags.objects.create(tag=tag)
    tag.model_ids.add(id_model)
    model_tags = list(Tags.objects.filter(model_ids=model_id).values())
    response = {"model_tags": model_tags}
    return JsonResponse(response, safe=False)

# Stránka pro editaci galerie modelu
@login_required(login_url="/log/in")
def editGallery(request, model_id):
    if request.method == "POST":
        form = FilesModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            if request.FILES:
                id_model = ObjectModel.objects.only("id").get(id=model_id)
                for f in request.FILES.getlist("f"):
                    Files.objects.create(model_id=id_model, f=f)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = FilesModelForm()
        gallery = get_list_or_404(Files, model_id=model_id)
        context = {"form": form, "imgs": gallery, "model_id": model_id}
        return render(request, "objectGallery/editGallery.html", context=context)
    

# Metoda pro vymazání modelu z databáze podle id
@login_required(login_url="/log/in")
def delete(request, model_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Nemáte oprávnění smazat model!")
        return HttpResponseRedirect(reverse("index"))
    else:
        model = ObjectModel.objects.get(pk=model_id)
        if model is not None: # Jestli model existuje, tak se smaže, jinak se vypíše chybová hláška
            model.delete() # Vymazání modelu
            # Přidat vymazání souborů modelu
            messages.success(request, "Model vymazán z databáze") # Zpráva o úspěchu
            return HttpResponseRedirect(reverse("index")) # Přesměrování na index
        else:
            messages.warning(request, "Model nebyl nalezen")
            return HttpResponseRedirect(reverse("index"))

# Metoda pro ajax na mazání modelu
@login_required(login_url="/log/in")
def ajaxDelete(request, model_id):
    model = ObjectModel.objects.get(pk=model_id)
    if model is not None: # Jestli model existuje, tak se smaže, jinak se vypíše chybová hláška
        model.delete() # Vymazání modelu
        # Přidat vymazání souborů modelu
        response = {"status": True, "id": model_id, "type": "Model"}
        return JsonResponse(response)
    else:
        response = {"status": False, "id": model_id, "type": "Model"}
        return JsonResponse(response)

# Metoda pro vymazání obrázku z galerie pomocí ID
@login_required(login_url="/log/in")
def deleteFromGallery(request, img_id):
    img = Files.objects.get(pk=img_id)
    if img is not None:
        img.delete()
        messages.success(request, "Obrázek smazán!")
        return HttpResponseRedirect(reverse("index"))
    else:
        messages.error(request, "Obrázek nebyl nalezen!")
        return HttpResponseRedirect(reverse("index"))

# Metoda pro vymazání obrázku z galerie pomocí ajax
@login_required(login_url="/log/in")
def ajaxDeleteFromGallery(request, img_id):
    img = Files.objects.get(pk=img_id)
    if img is not None:
        img.delete()
        response = {"status": True, "id": img_id, "type": "Obrázek"}
        return JsonResponse(response)
    else:
        response = {"status": False, "id": img_id, "type": "Obrázek"}
        return JsonResponse(response)

@login_required(login_url="/log/in")
def ajaxDeleteTag(request, model_id, tag_id):
    tag = get_object_or_404(Tags, pk=tag_id)
    model = get_object_or_404(ObjectModel, pk=model_id)
    tag.model_ids.remove(model)
    model_tags = list(Tags.objects.filter(model_ids=model_id).values())
    response = {"model_tags": model_tags}
    return JsonResponse(response, safe=False)

@login_required(login_url="/log/in")
def delall(request):
    return render(request, "objectGallery/delall.html")

@login_required(login_url="/log/in")
def deleteAll(request):
    models = ObjectModel.objects.all()
    for model in models:
        model.delete()
    messages.success(request, "VŠECHNY MODELY SMAZÁNY!")
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