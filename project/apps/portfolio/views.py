from django.shortcuts import render
from .models import Menu, Header

# Create your views here.


def index(request):
    menus = Menu.objects.all()
    header = Header.objects.first()
    context = {
        'menus': menus,
        'header': header,
    }
    return render(request, 'portfolio/index.html', context)
