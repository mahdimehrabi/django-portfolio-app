from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Menu, Header, About, Experience, Study, Project
from django.utils.translation import activate

# Create your views here.


def index(request):
    menus = Menu.objects.all()
    header = Header.objects.first()
    about = About.objects.first()
    experiences = Experience.objects.all()
    studies = Study.objects.all()
    projects = Project.objects.all()
    context = {
        'menus': menus,
        'header': header,
        'about': about,
        'experiences': experiences,
        'studies': studies,
        'projects': projects
    }
    return render(request, 'portfolio/index.html', context)


def language_switch(request, lang):
    activate(lang)
    return HttpResponseRedirect(reverse('portfolio:index'))
