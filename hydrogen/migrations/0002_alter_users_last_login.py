# Generated by Django 3.2.13 on 2022-05-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydrogen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]