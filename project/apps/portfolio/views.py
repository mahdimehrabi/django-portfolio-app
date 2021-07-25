from django.shortcuts import render
from .models import Menu

# Create your views here.


def index(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus
    }
    return render(request, 'portfolio/index.html', context)
