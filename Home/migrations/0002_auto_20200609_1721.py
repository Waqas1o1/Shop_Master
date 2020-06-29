# Generated by Django 3.0.6 on 2020-06-09 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_publishDate',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_titile', models.CharField(max_length=30)),
                ('item_FrashPricse', models.FloatField(max_length=30)),
                ('item_Discount_pricse', models.FloatField(max_length=30)),
                ('item_discription', models.TextField()),
                ('item_quantity', models.IntegerField()),
                ('item_publishDate', models.DateTimeField()),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Product')),
            ],
        ),
    ]
