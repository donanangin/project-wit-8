from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

# Create your views here.
def pengguna(request):
    return HttpResponse("Welcome to BookStore")
