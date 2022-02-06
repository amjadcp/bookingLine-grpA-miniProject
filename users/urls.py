from django.urls import path
from .views import *

app_name='users'
urlpatterns = [
    path('signup-client', signup_client, name='signup-client'),
    path('signup-serviceprovider', signup_serviceprovider, name='signup-serviceprovider'),
    path('profile', profile, name='profile'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard-client', dashboard_client, name='dashboard-client'),
]