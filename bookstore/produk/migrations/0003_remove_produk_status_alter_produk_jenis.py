# Generated by Django 4.2 on 2023-06-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0002_produk_penulis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='status',
        ),
        migrations.AlterField(
            model_name='produk',
            name='jenis',
            field=models.CharField(choices=[('Ebook', 'Ebook'), ('Buku', 'Buku')], default='Ebook', max_length=5),
        ),
    ]
