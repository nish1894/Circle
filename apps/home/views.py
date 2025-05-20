from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.

def home_view(request):
    return render(request, 'home/home.html', {})

