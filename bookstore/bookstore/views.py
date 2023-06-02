from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Selamat datang di halaman utama")

def pengguna(request):
    return HttpResponse("Welcome to BookStore")


def produk(request):
    return HttpResponse("Select Your Book")
