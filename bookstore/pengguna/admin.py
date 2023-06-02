from django.contrib import admin
from .models import Pengguna
# Register your models here.

class PenggunaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'password', 'alamat', 'tanggal_daftar')

admin.site.register(Pengguna, PenggunaAdmin)
