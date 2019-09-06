# Generated by Django 2.2.4 on 2019-09-03 12:31

import Product.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_auto_20190903_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default/no-image-icon.png', null=True, upload_to=Product.models.upload_to, verbose_name='Media'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.Product')),
            ],
            options={
                'verbose_name_plural': 'Product in Cart',
            },
        ),
    ]