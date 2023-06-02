# Generated by Django 4.2 on 2023-06-01 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produk', '0007_buku_harga_diskon_ebook_harga_diskon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='label',
            field=models.CharField(choices=[('NA', 'New Arrival'), ('BS', 'Best Seller'), ('DISC', 'Discount')], max_length=5),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.PositiveIntegerField()),
                ('total_harga', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tanggal_pemesanan', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.buku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]