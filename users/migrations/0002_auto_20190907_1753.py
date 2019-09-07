# Generated by Django 2.2.4 on 2019-09-07 14:53

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adress',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Adress:'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=31, null=True, verbose_name='Phone Number:'),
        ),
    ]
