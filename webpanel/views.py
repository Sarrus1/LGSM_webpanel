from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'webpanel/index.html')

def buttons(request):
    return render(request, 'webpanel/buttons.html')