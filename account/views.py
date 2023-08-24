from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import EditForm


def user_login(request):
    context = {"errors": []}
    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        username = username.strip().lower()
        password = request.POST.get('password')
        password = password.strip()
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home_app:home')
        else:
            context['errors'].append('Invalid Username or Password')
            return render(request, 'account/login.html', context)

    return render(request, 'account/login.html', {})


def user_register(request):
    context = {"errors": []}
    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        username = username.strip().lower()
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password1 = password1.strip()
        password2 = request.POST.get('password2')
        password2 = password2.strip()

        a = []
        user = User.objects.all()
        for use in user:
            a.append(use.username)
        if username in a:
            context['errors'].append('This username is exist')
            return render(request, "account/register.html", context)
        else:
            pass


        if password1 != password2:
            context['errors'].append('The passwords are not the same')
            return render(request, "account/register.html", context)
        else:
            pass

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home_app:home')
    return render(request, 'account/register.html')


def user_logout(request):
    logout(request)
    return redirect('home_app:home')


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    print(user)
    return render(request, 'account/profile.html', {'user': user})


def edit_profile(request):
    user = request.user
    form = EditForm(instance=user)
    if request.method == "POST":
        form = EditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, "account/edit.html", {"form": form})

def reset_password(request):
    if request.method == "POST":
        return redirect("account:email_code")
    return render(request, 'account/reset.html', {})

def email_code(request):
    context = {"errors": []}
    if request.method == "POST":
        context['errors'].append('Code is wrong!!!')
        return render(request, 'account/email_code.html', context)
    return render(request, 'account/email_code.html', context)
