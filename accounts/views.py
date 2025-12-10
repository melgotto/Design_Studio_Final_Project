from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello, world. You're at the accounts index.")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )

            if user:
                login(request, user)
                return redirect("dashboard:index")  # твоя панель

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "accounts/profile.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")