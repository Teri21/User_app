# Generated by Django 2.2 on 2021-05-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0003_auto_20210516_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]
