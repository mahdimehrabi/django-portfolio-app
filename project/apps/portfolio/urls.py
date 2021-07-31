from django.urls import path
from .views import index, language_switch

app_name = 'portfolio'
urlpatterns = [
    path('', index, name='index'),
    path('switch-lang/<str:lang>/', language_switch, name='switch-lang')
]
