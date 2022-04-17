from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request, newUser)
            messages.info(request, 'Successfully Registered...')

            return redirect("index")

        context = {
            "form": form
        }
        return render(request, "register.html", context)

    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request, "register.html", context)


def loginUser(request):

    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Username or Password is incorrect..")
            return render(request, "login.html", context)

        else:
            messages.success(request, "Successfully log in..")
            login(request, user)
            return redirect("index")

    else:
        return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully log out..")
    return redirect("index")
