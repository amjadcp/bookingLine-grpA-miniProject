from django.urls import path
from .views import *

app_name='home'

urlpatterns = [
    path('', index, name='index'),
    path('home', after_login, name='home')
]