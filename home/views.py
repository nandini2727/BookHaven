from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request,"home.html")
    # template=loader.get_template('home.html')
    # return HttpResponse(template.render())

def shop(request):
    return render(request, "shop.html")

def signin(request):
    return render(request, "signin.html")

def signup(request):
    print('this is signup')
    return render(request, "signup.html")

def contact(request):
    return render(request, "contact.html")

def cart(request):
    return render(request, "cart.html")