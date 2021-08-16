from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.views import View
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _
######
from .models import (Menu, Header, About, Experience,
                     Study, Project, Skill, Social,
                     ContactMessage)
from .forms import ContactMessageForm


# Create your views here.

class Index(View):
    def get(self, request):
        form = ContactMessageForm()
        return self.render(form, request)

    def post(self, request):
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, _("thank you , your message recceived and I will contact you soon"), extra_tags="alert")
            return redirect('portfolio:index')
        return self.render(form, request)

    def render(self, form, request):
        menus = Menu.objects.all()
        header = Header.objects.first()
        about = About.objects.first()
        experiences = Experience.objects.all()
        studies = Study.objects.all()
        projects = Project.objects.all()
        skills = Skill.objects.all()
        socials = Social.objects.all()
        context = {
            'menus': menus,
            'header': header,
            'about': about,
            'experiences': experiences,
            'studies': studies,
            'projects': projects,
            'skills': skills,
            'socials': socials,
            'form': form
        }
        return render(request, 'portfolio/index.html', context)


def language_switch(request, lang):
    activate(lang)
    return HttpResponseRedirect(reverse('portfolio:index'))
