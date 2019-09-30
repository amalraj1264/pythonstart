from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexpage(request):
    return HttpResponse("welcome to my inde page")
def contact(request):
    return HttpResponse("Contact page")
def home(request):
    return HttpResponse("Welcome to home page")