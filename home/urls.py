from django.urls import path
from .views import *

app_name='home'

urlpatterns = [
    path('', index, name='index'),
    path('home', after_login, name='home'),
    path('auditorium-info', auditorium_info, name='auditorium-info'),
    path('auditoriums', auditoriums, name='auditoriums'),
    path('auditorium-book', auditorium_book, name='auditorium-book'),
    path('contact', contact, name='contact'),
]