# Generated by Django 4.2.13 on 2024-07-24 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_sell',
            name='Fk',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Product_view', to='olx.product_view'),
        ),
    ]
