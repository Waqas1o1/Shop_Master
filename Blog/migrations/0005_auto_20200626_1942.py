# Generated by Django 3.0.6 on 2020-06-26 14:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_blog_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_quote_1',
            field=tinymce.models.HTMLField(blank=True, db_index=1),
        ),
    ]