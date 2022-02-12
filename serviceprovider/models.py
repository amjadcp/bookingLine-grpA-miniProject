import re
from django.db import models
from users.models import *
from .utils import *
# Create your models here.

class Auditorium(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    catelog = models.ImageField(upload_to=get_catelog_upload_to)
    about = models.TextField(max_length=300)
    number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    street = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=10)
    post = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}-{self.user}'


class Preview(models.Model):
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=get_preview_upload_to)

    def __str__(self) -> str:
        return f'{self.auditorium}'

class Book(models.Model):
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=30)
    book_number = models.CharField(max_length=15)
    book_email = models.EmailField()
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    message = models.TextField(max_length=200)
    connected = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.auditorium}'


