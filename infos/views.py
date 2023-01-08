from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    t = loader.get_template('infos/home.html')
    return HttpResponse(t.render({'title': 'Home'}))


def about(request):
    return HttpResponse("About me page")


def contact(request):
    return HttpResponse("Contact page")
