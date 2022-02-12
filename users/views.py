from django.http import HttpRequest
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date

from .forms import *
from .models import *
from serviceprovider.models import Auditorium, Book

# Create your views here.

#client
def signup_client(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print("Success")
            email = form.cleaned_data['email']
            form.save()
            user = User.objects.get(email=email)
            acc = AccType.objects.create(user=user, type='client')
            acc.save()
            return redirect('accounts/login')
    return render(request, 'signup_client.html', {'form': form})

#service provider
def signup_serviceprovider(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print("Success")
            email = form.cleaned_data['email']
            form.save()
            user = User.objects.get(email=email)
            acc = AccType.objects.create(user=user, type='serviceprovider')
            acc.save()
            return redirect('accounts/login')
    return render(request, 'signup_service.html', {'form': form})

@login_required(login_url='users:signup-serviceprovider')
def dashboard(request):
    user = User.objects.get(email=request.user)
    auditoriums = Auditorium.objects.filter(user=user)
    try:
        profile_status = ProfileStatus.objects.get(user=user)
        if profile_status.status == "Accepted":
            status = 'accepted'
        else:
            status = 'deline'
    except:
        status = 'pending'

    context = {
        'profile' : Profile.objects.get(user=user).pic,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'username' : user.username,
        'email' : user.email,
        'status' : status,
        'auditoriums': auditoriums,
        'date' : date.today()
    }
    
    return render(request, 'dashboard_service.html', context=context)

@login_required(login_url='users:signup-serviceprovider')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        adhar = request.POST['adhar']
        pdf_adhar = request.FILES['pdf_adhar']
        pic = request.FILES['pic']
        passbook = request.FILES['passbook']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        user = request.user
        profile = Profile.objects.create(
            user=user,
            name=name,
            phone=phone,
            email=email,
            adhar=adhar,
            pdf_adhar=pdf_adhar,
            pic=pic,
            passbook=passbook,
            address1=address1,
            address2=address2,
            district=district,
            state=state,
            pin=pin
        )
        profile.save()
        return redirect('users:dashboard')
    return render(request, 'profile.html', {'form': ProfileForm()})

@login_required(login_url='users:signup-client')
def dashboard_client(request):
    user = request.user
    books = Book.objects.filter(user=user)
    user = User.objects.get(email=user)
    context = {
        'books':books, 
        'user':user,
        'date' : date.today()
        }
    return render(request, 'dashboard_client.html', context=context)




