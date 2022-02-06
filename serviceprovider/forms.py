from dataclasses import field
from pyexpat import model
from django import forms
from .models import *
class DateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'book_name',
            'book_number',
            'book_email',
            'date', 
            'from_time', 
            'to_time'
            )

    def __init__(self, *args, **kargs):
        super(DateForm, self).__init__(*args, **kargs)
        self.fields['book_name'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Your Name'
        })
        self.fields['book_number'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Your Phone Number'
        })
        self.fields['book_email'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Your Email'
        })
        self.fields['date'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Date (YYYY-MM-DD)'
        })
        self.fields['from_time'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'From Time (HH:MM:SS)'
        })
        self.fields['to_time'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'To Time (HH:MM:SS)'
        })
        
