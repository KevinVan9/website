from django.shortcuts import render
from django.conf import settings
import os
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "polls/index.html")
    return HttpResponse("Hello, world. You're at the polls index.")

def get_pictures():
    image_list=[]
    static_dirs = settings.STATICFILES_DIRS
    print("settings:", settings.__dict__)
    print("static_dirs:", static_dirs)
    for dir in static_dirs:
        print("directory:", dir)
        for file in os.listdir(dir):
            print(file)
            if file.endswith(".png") or file.endswith(".jpg"):
                image_list.append(file)
    print(image_list)
    return image_list

def test_load(request):
    return render(request, "polls/test.html", {"img_list": get_pictures()})

def test_lazy_load(request):
    return render(request, "polls/test2.html", {"img_list": get_pictures()})

def popup(request):
    return render(request, "polls/popup.html")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)