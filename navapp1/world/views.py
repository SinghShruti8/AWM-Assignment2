from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic.base import TemplateView
import folium
from .models import Search


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, "registration/signup.html", context)


def index(request):
    return render(request, "index.html")



def maps(request):
    return render(request, "map.html")


def login(request):
    return render(request, "registration/login.html")
