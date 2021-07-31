from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Menu, Header, About
from django.utils.translation import activate

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


def language_switch(request, lang):
    activate(lang)
    return HttpResponseRedirect(reverse('portfolio:index'))
