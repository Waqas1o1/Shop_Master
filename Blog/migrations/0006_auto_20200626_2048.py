# Generated by Django 3.0.6 on 2020-06-26 15:48

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20200626_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_quote_1',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]