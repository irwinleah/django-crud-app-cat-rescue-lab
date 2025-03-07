# main_app/views.py

from django.shortcuts import render
from .models import Cat
# Import HttpResponse to send text-based responses
from django.http import HttpResponse


def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_detail(request, cat_id):
    cat = Cat.ojects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})
