from django.shortcuts import render, redirect
from Pak_Political_Trends.forms import RegistrationForm, TrendsInputForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'Pak_Political_Trends/index.html')


def about(request):
    return render(request, 'Pak_Political_Trends/about.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('userlogin')


@login_required
def trends_form(request):
    if request.method == 'GET':
        trends_input_form = TrendsInputForm(request.GET)

        if trends_input_form.is_valid():
            return redirect('/Pak_Political_Trends/')
    else:
        trends_input_form = TrendsInputForm()

    return render(request, 'Pak_Political_Trends/trends_form.html', {'trends_input_form': trends_input_form})


def user_registration(request):
    if request.method == 'POST':
        signup_form = RegistrationForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()
            return redirect('/Pak_Political_Trends/')
    else:
        signup_form = RegistrationForm()

    return render(request, 'Pak_Political_Trends/user_registration.html', {'signup_form': signup_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return HttpResponseRedirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect('index')

            else:
                HttpResponse("Account Is Not Active")
        else:
            HttpResponse("Invalid Login Credentials")
            return render(request, 'Pak_Political_Trends/userlogin.html')
    else:
        return render(request, 'Pak_Political_Trends/userlogin.html')
