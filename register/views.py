from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .deco import *

# Create your views here.
@unauthenticated_user
def membership(request):
    return render(request, 'register/membership.html')
@unauthenticated_user
def create_account_page(request):
    form = UserForm()
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            username = request.POST.get('username') 
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Thank you for join our website "'+username+'" enjoy 🥳')
            return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'register/create_account_page.html', context)

@unauthenticated_user
def login_page(request):
    if request.method=='POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome Back "'+username+'"' )
            return redirect(reverse('main:articles'))
        else:
            messages.error(request, 'Username or password is incorrect !')
    return render(request, 'register/login_page.html')


def logout_page(request):
    logout(request)
    return redirect(reverse('main:articles'))


def profile(request):
    user = request.user.profile
    context = {
        'user':user
    }
    return render(request, 'register/profile.html', context)

def edit_profile(request):
    data = request.user.profile
    form = ProfileForm(instance=data)
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            new_form = form.save()
            new_form.user = request.user
            new_form.save()
            return redirect('/accounts/profile/')
            
            
    context = {
        'form':form
    }
    return render(request, 'register/edit_profile.html', context)


def change_password(request):
    form = CustomPasswordChange(user=request.user)
    if request.method=='POST':
        form = CustomPasswordChange(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # that code code above mean that if you change the password while you're logging in you keep your accounts login
            return redirect('/accounts/profile/')
    context={
        'form':form
    }
    return render(request, 'register/change_password.html', context)





    