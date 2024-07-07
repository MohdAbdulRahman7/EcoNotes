from django.http import HttpResponse
from django.shortcuts import render # this is used to render templates when view function is invoked


def homepage(request):
    #return HttpResponse('My Home Page!') -- instead of this, render a template (home.html)
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')