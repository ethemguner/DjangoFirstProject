# Generated by Django 2.2.4 on 2019-09-08 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190908_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cart',
        ),
    ]