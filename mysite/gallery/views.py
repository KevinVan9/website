from django.shortcuts import render
from django.conf import settings
import os
# Create your views here.
from django.http import HttpResponse

def get_pictures():
    image_list=[]
    static_dirs = settings.STATICFILES_DIRS
    for dir in static_dirs:
        for file in os.listdir(dir):
            if file.endswith(".png") or file.endswith(".jpg"):
                image_list.append(file)
    return image_list


def index(request):
    return render(request, "gallery/index.html")

def home(request):
    return render(request, "gallery/home.html")

def test_load(request):
    return render(request, "gallery/test.html", {"img_list": get_pictures()})

def test_lazy_load(request):
    return render(request, "gallery/test2.html", {"img_list": get_pictures()})

def popup(request):
    return render(request, "gallery/popup.html")

def navigation_bar(request):
    return render(request, "gallery/navigation-bar.html")

def viewer(request):
    return render(request, "gallery/viewer.html", {"img_list": get_pictures()})