from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required
def add_auditorium(request):
    if request.method == 'POST':
        user = request.user
        email = ''
        name = request.POST['name']
        catelog = request.FILES.get('catelog')
        about = request.POST['about']
        number = request.POST['number']
        email = request.POST['email']
        price = request.POST['price']
        street = request.POST['street']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        post = request.POST['post']
        images = request.FILES.getlist('images')

        Auditorium.objects.create(
            user = user,
            name = name,
            catelog = catelog,
            about = about,
            number = number,
            email = email,
            price = price,
            street = street,
            district = district,
            state = state,
            pin = pin,
            post = post
        )

        auditoriums = Auditorium.objects.filter(user=user)
        for auditorium in auditoriums:
            if auditorium.name == name:
                for image in images:
                    Preview.objects.create(
                        auditorium = auditorium,
                        images = image
                    )        
        return redirect('users:dashboard')

    return render(request, 'auditorium.html')

@login_required
def auditorium_dashboard(request, user, id):
    auditorium = Auditorium.objects.get(id=id)
    books = Book.objects.filter(auditorium=auditorium)
    context = {'auditorium':auditorium, 'books':books}
    return render(request, 'auditorium_dashboard.html', context=context)

@login_required
def update_auditorium(request,id):
    if request.method == 'POST':
        auditorium = Auditorium.objects.get(id=id)
        user = request.user
        auditorium.name = request.POST['name']
        catelog = request.FILES.get('catelog')
        if catelog != None:
            auditorium.catelog = catelog
        auditorium.about = request.POST['about']
        auditorium.number = request.POST['number']
        auditorium.email = request.POST['email']
        auditorium.price = request.POST['price']
        auditorium.street = request.POST['street']
        auditorium.district = request.POST['district']
        auditorium.state = request.POST['state']
        auditorium.pin = request.POST['pin']
        auditorium.post = request.POST['post']
        auditorium.save()
        images = request.FILES.getlist('images')

        if images != []:
            previews = Preview.objects.filter(auditorium=auditorium) 
            for preview in previews:
                preview.delete()

            for image in images:
                Preview.objects.create(
                    auditorium = auditorium,
                    images = image
                )  
        return redirect(f'../auditorium-dashboard/{request.user}/{id}')

        
    data = Auditorium.objects.get(id=id)
    return render(request, 'update_auditorium.html', {'data' : data})