# Generated by Django 2.2 on 2021-06-04 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]