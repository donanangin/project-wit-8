from django.contrib import admin
from .models import Buku, Ebook, OrderProdukItem, Order, AlamatPengiriman, Payment

class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul_buku', 'penulis', 'harga', 'harga_diskon', 'slug', 'deskripsi', 'gambar', 'label', 'kategori', 'jenis')
    verbose_name_plural = "Buku"
    verbose_name = "Buku"

class EbookAdmin(admin.ModelAdmin):
    list_display = ('judul_buku', 'penulis', 'harga', 'harga_diskon', 'slug', 'deskripsi', 'gambar', 'label', 'kategori', 'jenis')
    verbose_name_plural = "Ebook"
    verbose_name = "Ebook"

class OrderProdukItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'buku_item', 'ebook_item', 'ordered')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'jumlah', 'total_harga', 'tanggal_pemesanan', 'status')

class AlamatPengirimanAdmin(admin.ModelAdmin):
    list_display = ('user', 'alamat_1', 'alamat_2', 'negara', 'kode_pos')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'timestamp', 'payment_option', 'charge_id')

admin.site.register(Buku, BukuAdmin)
admin.site.register(Ebook, EbookAdmin)
admin.site.register(OrderProdukItem, OrderProdukItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(AlamatPengiriman, AlamatPengirimanAdmin)
admin.site.register(Payment, PaymentAdmin)