# Generated by Django 2.2.4 on 2019-09-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_auto_20190903_1542'),
        ('users', '0007_remove_profile_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cart',
            field=models.ManyToManyField(null=True, to='Product.Cart'),
        ),
    ]
