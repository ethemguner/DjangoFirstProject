# Generated by Django 2.2.4 on 2019-09-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190908_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='adress',
            field=models.TextField(blank=True, help_text='Your shipping adress.', max_length=1000, null=True, verbose_name='Adress:'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Notifications will send to your phone number.', max_length=10, null=True, verbose_name='Phone Number'),
        ),
    ]
