# Generated by Django 2.2.4 on 2019-09-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20190908_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart',
            field=models.ManyToManyField(null=True, to='Product.Cart'),
        ),
    ]