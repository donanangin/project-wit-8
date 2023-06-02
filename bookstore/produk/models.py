from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify

# Create your models here.
class Buku(models.Model):
    EBOOK = 'Ebook'
    BUKU = 'Buku'

    JENIS_PRODUK = (
        (BUKU, 'Buku'),
        (EBOOK, 'Ebook'),
    )


    PILIHAN_LABEL = [
        ('NA', 'New Arrival'),
        ('BS', 'Best Seller'),
        ('DISC', 'Discount'),
    ]


    PILIHAN_KATEGORI = [
        ('Self-Development', 'Self-Development'),
        ('Literacy Financial', 'Literacy Financial'),
        ('Technology', 'Technology'),
        ('College', 'College')
    ]

    judul_buku = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100, default='Unknown')
    harga = models.DecimalField(max_digits=8, decimal_places=2)
    harga_diskon = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='product_pics')
    label = models.CharField(choices=PILIHAN_LABEL, max_length=4)
    kategori = models.CharField(choices=PILIHAN_KATEGORI, max_length=100)
    jenis = models.CharField(max_length=5, choices=JENIS_PRODUK, default=EBOOK)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul_buku)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.judul_buku} - Rp{self.harga}"
    
    class Meta:
        verbose_name_plural = 'Buku'
    

class Ebook(models.Model):
    EBOOK = 'Ebook'
    BUKU = 'Buku'


    JENIS_PRODUK = (
        (BUKU, 'Buku'),
        (EBOOK, 'Ebook'),
    )


    PILIHAN_LABEL = [
        ('NA', 'New Arrival'),
        ('BS', 'Best Seller'),
        ('DISC', 'Discount'),
    ]


    PILIHAN_KATEGORI = [
        ('Self-Development', 'Self-Development'),
        ('Literacy Financial', 'Literacy Financial'),
        ('Technology', 'Technology'),
        ('College', 'College')
    ]

    judul_buku = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100, default='Unknown')
    harga = models.DecimalField(max_digits=8, decimal_places=2)
    harga_diskon = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='product_pics')
    label = models.CharField(choices=PILIHAN_LABEL, max_length=5)
    kategori = models.CharField(choices=PILIHAN_KATEGORI, max_length=100)
    jenis = models.CharField(max_length=5, choices=JENIS_PRODUK, default=EBOOK)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul_buku)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.judul_buku} - Rp{self.harga}"
    
    class Meta:
        verbose_name_plural = 'Ebook'

class OrderProdukItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    buku_item = models.ForeignKey(Buku, on_delete=models.CASCADE, null=True, blank=True)
    ebook_item = models.ForeignKey(Ebook, on_delete=models.CASCADE, null=True, blank=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produk = models.ManyToManyField(OrderProdukItem)
    jumlah = models.PositiveIntegerField()
    total_harga = models.DecimalField(max_digits=8, decimal_places=2)
    tanggal_pemesanan = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order ID: {self.id}"
    
class AlamatPengiriman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alamat_1 = models.CharField(max_length=100)
    alamat_2 = models.CharField(max_length=100)
    negara = models.CharField(max_length=100)
    kode_pos = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - Alamat Pengiriman"

class Payment(models.Model):
    PILIHAN_PEMBAYARAN = [
        ('O1', 'Option 1'),
        ('O2', 'Option 2'),
        ('O3', 'Option 3'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_option = models.CharField(choices=PILIHAN_PEMBAYARAN, max_length=2)
    charge_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - Payment"