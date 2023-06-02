# Generated by Django 4.2 on 2023-06-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=100)),
                ('tanggal_daftar', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Pengguna',
                'ordering': ['-tanggal_daftar'],
            },
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_buku', models.CharField(max_length=100)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=8)),
                ('slug', models.SlugField(unique=True)),
                ('deskripsi', models.TextField()),
                ('gambar', models.ImageField(upload_to='product_pics')),
                ('label', models.CharField(choices=[('LBL1', 'Label 1'), ('LBL2', 'Label 2'), ('LBL3', 'Label 3'), ('LBL4', 'Label 4'), ('LBL5', 'Label 5'), ('LBL6', 'Label 6'), ('LBL7', 'Label 7'), ('LBL8', 'Label 8'), ('LBL9', 'Label 9'), ('LBL10', 'Label 10'), ('LBL11', 'Label 11'), ('LBL12', 'Label 12'), ('LBL13', 'Label 13'), ('LBL14', 'Label 14'), ('LBL15', 'Label 15'), ('LBL16', 'Label 16'), ('LBL17', 'Label 17'), ('LBL18', 'Label 18'), ('LBL19', 'Label 19'), ('LBL20', 'Label 20')], max_length=5)),
                ('kategori', models.CharField(max_length=100)),
                ('status', models.BooleanField(choices=[('Beli', 'Beli'), ('Pinjam', 'Pinjam')], max_length=6)),
                ('jenis', models.CharField(choices=[('Buku', 'Buku'), ('E-book', 'E-book')], max_length=100)),
            ],
        ),
    ]
