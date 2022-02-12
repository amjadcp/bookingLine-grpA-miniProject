from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from serviceprovider.models import Book, Preview
from users.models import *
from users.views import *
from .models import Contact
import random
# from serviceprovider.forms import *
# Create your views here.

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
    return redirect('home:index')

def index(request):
    context = {'check' : True}
    return render(request, 'index.html', context=context)

@login_required
def after_login(request):
    users = User.objects.all()
    user = request.user
    acc_type = AccType.objects.get(user=user)
    if acc_type.type == 'serviceprovider':
        try:
            status = Profile.objects.get(user=user)
        except:
            return redirect('users:profile')
        return redirect('users:dashboard')
    else:
        try:
            user = random.choice(users)
        except IndexError:
            return redirect('home:auditoriums')
        auditoriums_ = Auditorium.objects.filter(user=user)
        try:
            auditorium = random.choice(auditoriums_)
        except IndexError:
            return redirect('home:auditoriums')
        previews = Preview.objects.filter(auditorium=auditorium)
        context = {
                    'client':request.user,
                    'check' : False,
                    'auditorium' : auditorium,
                    'previews' : previews,
                    'preview0' : previews[0]
                }
        return render(request, 'home.html', context=context)
        
# @login_required
def auditoriums(request):
    list = Auditorium.objects.all()
    return render(request, 'auditoriums.html', {'list': list})

@login_required(login_url='users:signup-client')
def auditorium_info(request):
    if request.method == "POST":
        id = request.POST['btn']
        auditorium = Auditorium.objects.get(id=id)
        previews = Preview.objects.filter(auditorium=auditorium)
   
    context = {
        'auditorium' : auditorium,
        'client' : request.user,
        'previews' : previews,
        'preview0' : previews[0],
        'years' : list(range(2022,2051)),
        'months' : list(range(1,13)),
        'days' : list(range(1,32)),
        'froms' : list(range(7, 23)),
        'tos' : list(range(8, 24)),
    }
    return render(request, 'auditorium_info.html', context=context)

@login_required(login_url='users:signup-client')
def auditorium_book(request):
    if request.method == 'POST':
        id = request.POST['id']
        auditorium = Auditorium.objects.get(id=id)
        book_name = request.POST['book_name']
        book_number = request.POST['book_number']
        book_email = request.POST['book_email']
        year = request.POST['year']
        month = request.POST['month']
        day = request.POST['day']
        date = f'{year}-{month}-{day}'
        from_time = request.POST['from_time']
        from_time = str(from_time)+':00:00'
        to_time = request.POST['to_time']
        to_time = str(to_time)+':00:00'
        message = request.POST['message']
        books = Book.objects.filter(auditorium=auditorium)
        for book in books:
            if str(book.date) == date:
                if str(book.from_time)==from_time or str(book.to_time)>from_time:
                    print("Time slot not available")
                    return JsonResponse({'message' : '0'})
                
        Book.objects.create(
            auditorium=auditorium,
            user = request.user,
            book_name=book_name,
            book_number=book_number,
            book_email=book_email,
            date=date,
            from_time=from_time,
            to_time=to_time,
            message=message
        )

        
        send_mail(
            f'Booking Request from {request.user}(bookingLine)',
            f'''Name : {book_name}
            Contact Number : {book_number}
            Contact Email : {book_email}
            Date : {date}
            Time Slot : {from_time} - {to_time}
            Message : {message}''',
            'calicut673007@gmail.com',
            ['calicut673007@gmail.com', auditorium.user],
            fail_silently=False,
        )
        send_mail(
            f'Booking Request Send (bookingLine)',
            f'''Auditorium : {auditorium.name}
            Name : {book_name}
            Contact Number : {book_number}
            Contact Email : {book_email}
            Date : {date}
            Time Slot : {from_time} - {to_time}
            Message : {message}
            
            Service Provider will be contact you soon
            (bookingLine)''',
            'calicut673007@gmail.com',
            [request.user, 'calicut673007@gmail.com'],
            fail_silently=False,
        )
    return JsonResponse({'message' : '1'})

@login_required(login_url='users:signup-client')
def auditorium_cancel(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    send_mail(
            f'Booking Request Canceled by {request.user}(bookingLine)',
            f'''Name : {book.book_name}
            Contact Number : {book.book_number}
            Contact Email : {book.book_email}
            Date : {book.date}
            Time Slot : {book.from_time} - {book.to_time}
            Message : {book.message}

            {request.user} canceled their time slot
            (bookingLine)''',
            'calicut673007@gmail.com',
            [book.auditorium.user, 'calicut673007@gmail.com'],
            fail_silently=False,
    )
    send_mail(
        f'Booking Cancel Request Send (bookingLine)',
        f'''Auditorium : {book.auditorium.name}
        Name : {book.book_name}
        Contact Number : {book.book_number}
        Contact Email : {book.book_email}
        Date : {book.date}
        Time Slot : {book.from_time} - {book.to_time}
        Message : {book.message}
        
        Your time slot canceled
        (bookingLine)''',
        'calicut673007@gmail.com',
        [request.user, 'calicut673007@gmail.com'],
        fail_silently=False,
    )
    return redirect('users:dashboard-client')

@login_required(login_url='users:signup-client')
def connected(request,id):
    book = Book.objects.get(id=id)
    book.connected = True
    book.save()
    return redirect(f'../serviceprovider/auditorium-dashboard/{book.auditorium.user}/{book.auditorium.id}')

@login_required(login_url='users:signup-client')
def remove(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(f'../serviceprovider/auditorium-dashboard/{book.auditorium.user}/{book.auditorium.id}')



