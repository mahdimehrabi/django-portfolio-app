from django.shortcuts import render
from .models import Menu, Header, About

# Create your views here.


def index(request):
    menus = Menu.objects.all()
    header = Header.objects.first()
    about = About.objects.first()
    context = {
        'menus': menus,
        'header': header,
        'about': about
    }
    return render(request, 'portfolio/index.html', context)
