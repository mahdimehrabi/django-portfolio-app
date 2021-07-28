from django.contrib import admin
from .models import Menu, HeaderButton, Header

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


admin.site.register(Menu, MenuAdmin)
admin.site.register(Header, HeaderAdmin)
