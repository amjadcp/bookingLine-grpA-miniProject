from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .utils import *


class User(AbstractUser):
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'

class AccType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    adhar = models.CharField(max_length=12)
    pdf_adhar = models.FileField(upload_to=get_aadhar_upload_to, null= False,)
    pic = models.ImageField(upload_to=get_pic_upload_to, null=False)
    passbook = models.ImageField(upload_to=get_passbook_upload_to, null=False)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.user}'

class ProfileStatus(models.Model):
    choices = (
        ('Accepted', 'Accepted'),
        ('Deline', 'Deline')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=9, choices=choices)

    def __str__(self):
        return f'{self.user}'