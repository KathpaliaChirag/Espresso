# Generated by Django 4.1.3 on 2022-12-01 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Esetup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='session_id',
        ),
    ]
