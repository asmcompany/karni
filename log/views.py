from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User



def home_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    context = {
        "title": "صفحه اصلی",
        "content": "خوش امدید",
        "brand": "Topleaarn Eshop From Views.py"
    }
    if request.user.is_authenticated:
        context["new_content"] = "this is new content"
    return render(request, "index.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name_l = login_form.cleaned_data.get('user_name_l')
        password_l = login_form.cleaned_data.get('password_l')
        user = authenticate(request, username=user_name_l, password=password_l)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name_l', 'کاربر یافت نشد')
    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/')

    context = {
        'register_form':
            register_form
    }
    return render(request, 'register.html', context)


def logout_user(request):
    auth.logout(request)
    return redirect('/')

