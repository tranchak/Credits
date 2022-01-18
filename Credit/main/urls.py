from django.urls import path

from .views import get_bank, get_home

app_name = 'main'
urlpatterns = [
    path('', get_home, name='get_home'),
    path('banks', get_bank, name='get_bank'),

]
