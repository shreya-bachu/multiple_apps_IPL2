from django.shortcuts import render
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> ruturaj is captain of csk')

# Create your views here.
