from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    t = loader.get_template('infos/home.html')
    return HttpResponse(t.render({'title': 'Home'}))


def about(request):
    t = loader.get_template('infos/about.html')
    return HttpResponse(t.render({'title': 'About'}))


def contact(request):
    t = loader.get_template('infos/contact.html')
    return HttpResponse(t.render({'title': 'Contact'}))
