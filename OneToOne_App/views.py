
from django.shortcuts import render
from django.http import HttpResponse
def home_view(request):
    message = 'Welcome to Home Page'
    return HttpResponse(message)


