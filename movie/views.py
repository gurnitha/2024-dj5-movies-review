# movie/views.py
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home_view(request):
    # return render(request, 'home.html', {'nama_saya': 'I NYOMAN GURNITHA' })
    return render(request, 'movie/home.html', {'nama_saya': 'I NYOMAN GURNITHA' })

def about_view(request):
    # return render(request, 'about.html')
    return render(request, 'movie/about.html')