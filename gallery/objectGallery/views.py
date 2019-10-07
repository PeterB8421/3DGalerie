from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.urls import reverse
from .models import ObjectModel
from .forms import ObjectModelForm
from objectGallery.forms import ObjectModelForm


def index(request):
    objectList = get_list_or_404(ObjectModel)
    context = {'models': objectList}
    messages.info(request, "Hello world")
    return render(request, 'objectGallery/index.html', context)

def detail(request, model_id):
    return HttpResponse("Na této stránce bude výpis konkrétního objektu")

def create(request):
    if request.method == "POST":
        form = ObjectModelForm(request.POST, request.FILES)
        if form.is_valid():
            obj_file = form.cleaned_data["obj_file"]
            mtl_file = form.cleaned_data["mtl_file"]
            fs = FileSystemStorage()
            fs.save(obj_file.name, obj_file)
            fs.save(mtl_file.name, mtl_file)
            form.save()
            messages.success(request, "Objekt úspěšně přidán do databáze")
            return HttpResponseRedirect(reverse("index"))

    else:
        form = ObjectModelForm()
    return render(request, "objectGallery/create.html", {"form": form})

def edit(request, model_id):
    return HttpResponse("Zde bude stránka pro editaci objektu")