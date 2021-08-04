from django.contrib import admin
from .models import (Menu, HeaderButton, Header, About, Experience,
                     Study, Project, Skill)


# Register your models here.


class HeaderButtonInline(admin.TabularInline):
    model = HeaderButton
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_fa')


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('first_title', 'second_title')
    inlines = [HeaderButtonInline]

    def has_delete_permission(self, request, obj=None):
        return False


class AboutAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('employer_name', 'job_title')


class StudyAdmin(admin.ModelAdmin):
    list_display = ('university_title', 'study_grade')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_fa')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_fa')


admin.site.register(Menu, MenuAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Skill, SkillAdmin)