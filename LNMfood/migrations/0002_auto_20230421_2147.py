# Generated by Django 3.2.5 on 2023-04-21 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LNMfood', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_food',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blog_food',
            name='fare',
        ),
        migrations.RemoveField(
            model_name='blog_food',
            name='time',
        ),
    ]
