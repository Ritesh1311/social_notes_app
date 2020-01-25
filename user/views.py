from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {"heading:Social Notes App"}
    return render(request,'index.html')