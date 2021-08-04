from django.urls import path
from .views import Index, language_switch

app_name = 'portfolio'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('switch-lang/<str:lang>/', language_switch, name='switch-lang'),
]
