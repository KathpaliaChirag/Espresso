# Generated by Django 4.1.1 on 2022-11-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esetup', '0002_customuser_display_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='display_pic',
            field=models.ImageField(default='', upload_to='displaypic'),
        ),
    ]
