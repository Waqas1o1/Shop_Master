# Generated by Django 3.0.6 on 2020-06-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_product_product_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_baneer',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
