# Generated by Django 2.2.4 on 2019-09-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_auto_20190903_1542'),
        ('users', '0011_auto_20190908_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cart',
        ),
        migrations.AddField(
            model_name='profile',
            name='cart',
            field=models.ManyToManyField(null=True, to='Product.Product'),
        ),
    ]
