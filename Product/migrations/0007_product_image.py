# Generated by Django 2.2.4 on 2019-09-02 14:54

import Product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_product_added_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default/no-image-icon.png', null=True, upload_to=Product.models.upload_to, verbose_name='Media:'),
        ),
    ]
