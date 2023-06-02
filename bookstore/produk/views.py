from django.shortcuts import render
from .models import Buku
from django.http import HttpResponse

# Create your views here.
def produk(request):
    return HttpResponse("Select Your Book")

def produk_list(request):
    produk = Buku.objects.all()
    context = {
        'produk_list': produk,  # Rename the context variable to 'produk_list'
        'produk_name': 'Book'  # Add a new context variable 'produk_name'
    }
    return render(request, 'produk_list.html', context)

def produk_detail(request, slug):
    produk = Buku.objects.get(slug=slug)
    context = {
        'produk': produk
    }
    return render(request, 'produk_detail.html', context)

