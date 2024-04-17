from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

from .models import *


# Create your views here.

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,subject=desc,phone=phone,date=datetime.today())
        contact.save()

    return render(request, 'contact.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    form=UserCreationForm()
    context={'form':form}
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            

            return redirect('home')
    return render(request, 'signup.html',context)

