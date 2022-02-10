from django.http import HttpRequest
from django.shortcuts import render, redirect
import requests, json
# Create your views here.

def index(request):
    url="https://api.chucknorris.io/jokes/random"
    response = requests.request("GET", url).json()
    joke = response['value']
    return render(request, 'index.html', {'joke':joke});

def get_joke(request):
   if request.method == 'POST':
        category = request.POST['categories']
        response = requests.request("GET", url=f"https://api.chucknorris.io/jokes/random?category={category}").json()
        category_joke = response['value']
        return render(request, 'index.html', {'category_joke': category_joke})# Redirect after POST
        
        
    