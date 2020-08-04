from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import  password_validation


class UserForm(UserCreationForm):
    email_error_messages = {
        'email_is_not_unique':('The email is already exist !'),
    }
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                        'placeholder':'password',
                                        'required': 'true',

        })
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                        'placeholder':'Enter the same password as above, for verification.',
                                        'type': 'password',
                                        'required': 'true',
        })
    )
    email = forms.CharField(
        label=("Email"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                    'type': 'email',
                                    'placeholder': 'Email address',
                                    'required': 'true'
        })
    )
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
        }



    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.email_error_messages['email_is_not_unique'],
                code='email_is_not_unique',
            )
        return email

        


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','name':'first_name','id':'first_name', 'placeholder':'first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','name':'last_name','id':'last_name', 'placeholder':'last name'}),
            'email':forms.TextInput(attrs={'class':'form-control','name':'email','id':'email', 'placeholder':'you@gmail.com'}),
            'phone':forms.TextInput(attrs={'class':'form-control','name':'phone','id':'phone', 'placeholder':'enter phone'}),
            'city':forms.TextInput(attrs={'class':'form-control','name':'location','id':'location', 'placeholder':'Somewhere'}),
            'bio':forms.Textarea(attrs={'class':'form-control' ,'placeholder':'Bio'}),
            'image':forms.FileInput(attrs={'class':'custom-file-input','id':'inputGroupFile01'}),
            'profession':forms.TextInput(attrs={'class':'form-control','name':'profession','id':'profession', 'placeholder':'what is your profession'}),
            'skills':forms.SelectMultiple(attrs={'class':'form-control','id':'exampleFormControlSelect2'},)
        }
    


class CustomPasswordChange(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect':
                "The old password is not correct. Please try again."}
    password_error_messages = {
        'password_mismatch': ('The two password fields didn’t match.'),
    }
    old_password = forms.CharField(required=True, label='Old Password',
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter you old password ..'
                    }),
                    error_messages={
                    'required': 'The password can not be empty'})

    new_password1 = forms.CharField(required=True, label='New Password',
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter you New password ..'
                    }),
                    error_messages={
                    'required': 'The password can not be empty'})
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Confirm you New password ..'
                    }),
                    error_messages={
                    'required': 'The password can not be empty'})

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.password_error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2




