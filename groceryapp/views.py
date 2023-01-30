from django.shortcuts import render
from .models import Carousel

# Create your views here.



def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'navigation.html')

def about(request):
    return render(request, 'about.html')

def main(request):
    data = Carousel.objects.all()
    dic={'data':data}
    return render(request, 'index.html',dic)