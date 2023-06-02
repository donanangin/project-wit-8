from django.urls import path
from produk import views

urlpatterns = [
    path('produk/', views.produk, name='buku')
]
