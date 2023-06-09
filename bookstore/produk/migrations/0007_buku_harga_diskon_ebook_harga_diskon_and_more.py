# Generated by Django 4.2 on 2023-06-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0006_alter_buku_options_alter_ebook_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='harga_diskon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ebook',
            name='harga_diskon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='label',
            field=models.CharField(choices=[('NA', 'New Arrival'), ('BS', 'Best Seller'), ('DISC', 'Discount')], max_length=4),
        ),
    ]
