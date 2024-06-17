from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import *

# Create your views here.

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def child(request):
    return render(request, 'child.html')


def children(request):
    return render(request, 'childgallery.html')


def com(request):
    return render(request, 'com.html')

def commni(request):
    return render(request, 'commni.html')

def contact(request):
    return render(request, 'contact.html')

def event(request):
    return render(request, 'event.html')

def health(request):
    return render(request, 'health.html')

def help(request):
    return render(request, 'help.html')

def sabbat(request):
    return render(request, 'sabbat.html')

def sti(request):
    return render(request, 'sti.html')

def study(request):
    return render(request, 'study.html')

def wome(request):
    return render(request, 'wome.html')

def women(request):
    return render(request, 'women.html')

def you(request):
    return render(request, 'you.html')


def youth(request):
    return render(request, 'youth.html')


def handleContactForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')

        obj = Contact.objects.create(name=name, phone=phone, email=email, address=address, message=message)
        obj.save()
        
        return JsonResponse(data={'status':200})
    
