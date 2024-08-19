from django.shortcuts import render # here by default
from django.http import HttpResponse # new# Create your views here.


def homePageView(request): # new
    return HttpResponse('Hello World!') # new
