from django.http import HttpRequest
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

# Create your views here.

#client
def signup_client(request):
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
    return render(request, 'signup_client.html', {'form': SignupForm()})

#service provider
def signup_serviceprovider(request):
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
    return render(request, 'signup_service.html', {'form': SignupForm()})

@login_required
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
    return render(request, 'profile.html', {'form': ProfileForm()})




