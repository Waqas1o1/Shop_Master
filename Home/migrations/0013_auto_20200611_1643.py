# Generated by Django 3.0.6 on 2020-06-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20200610_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_baneer',
            field=models.ImageField(upload_to=''),
        ),
    ]
