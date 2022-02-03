from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *



class SignupForm(UserCreationForm):
    class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') 
    def __init__(self, *args, **kargs):
        super(SignupForm, self).__init__(*args, **kargs)
        self.fields['username'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Username'
        })

        self.fields['first_name'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'First Name',
            'name' : 'first_name',
            'id' : 'first_name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Last Name',
            'name' : 'last_name',
            'id' : 'last_name',
        })
        self.fields['email'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Email',
            'name' : 'email',
            'id' : 'email',
        })

        self.fields['password1'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Password',
            'name' : 'password1',
            'id' : 'password1',
        })

        self.fields['password2'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Confirm Password',
            'name' : 'password2',
            'id' : 'password2',
        })
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'name', 'phone', 'email', 'adhar', 'pdf_adhar', 'pic', 'passbook',
            'address1', 'address2', 'district', 'state', 'pin'
        ) 
    def __init__(self, *args, **kargs):
        super(ProfileForm, self).__init__(*args, **kargs)
        self.fields['name'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Name',
            'name' : 'name',
            'id' : 'name'
        })
        self.fields['phone'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Phone Number',
            'name' : 'phone',
            'id' : 'phone'
        })
        self.fields['email'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Email',
            'name' : 'email',
            'id' : 'email'
        })
        self.fields['adhar'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Aadhar',
            'name' : 'adhar',
            'id' : 'adhar'
        })
        self.fields['pdf_adhar'].widget.attrs.update({
            'class' : 'form-control',
            'name' : 'pdf_adhar',
            'id' : 'pdf_adhar'
        })
        self.fields['pic'].widget.attrs.update({
            'class' : 'form-control',
            'name' : 'pic',
            'id' : 'pic'
        })
        self.fields['passbook'].widget.attrs.update({
            'class' : 'form-control',
            'name' : 'passbook',
            'id' : 'passbook'
        })
        self.fields['address1'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Address1',
            'name' : 'address1',
            'id' : 'address1'
        })
        self.fields['address2'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Address2',
            'name' : 'address2',
            'id' : 'address2'
        })
        self.fields['district'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'District',
            'name' : 'district',
            'id' : 'district'
        })
        self.fields['state'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'State',
            'name' : 'state',
            'id' : 'state'
        })
        self.fields['pin'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'PIN code',
            'name' : 'pin',
            'id' : 'pin'
        })
        