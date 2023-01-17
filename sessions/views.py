from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def set_session(request):
    request.session['sname'] = 'Django'
    request.session['semail'] = 'django@reinhard.com'
    return HttpResponse("session is set")


def get_session(request):
    student_name = request.session['sname']
    student_email = request.session['semail']
    return HttpResponse(f"{student_name} {student_email}")
