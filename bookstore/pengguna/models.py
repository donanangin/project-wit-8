from django.db import models

class Pengguna(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    tanggal_daftar = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Pengguna"
        ordering = ["-tanggal_daftar"]



