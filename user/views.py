from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('notes:list')
    else:
        form = UserCreationForm()
        return render(request,'index.html',{'form':form})