from unicodedata import name
from django.urls import path
from .views import *

app_name='serviceprovider'
urlpatterns = [
    path('add-auditorium', add_auditorium, name='add-auditorium'),
    path('update-auditorium/<int:id>', update_auditorium, name='update-auditorium'),
    path('auditorium-dashboard/<str:user>/<int:id>', auditorium_dashboard, name='auditorium-dashboard'),
]