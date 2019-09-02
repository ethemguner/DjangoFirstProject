from django.db import models
from unidecode import unidecode
from django.template.defaultfilters import slugify
from uuid import uuid4
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    price = models.IntegerField(null=True, blank=False)
    description = models.TextField(max_length=3000, null=True, blank=False, help_text="1000 characters limit.")
    slug = models.SlugField(null=True, unique=True, editable=False)
    added_date = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "{}".format(self.title)

    def get_unique_slug(self):
        number = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Product.objects.filter(slug=new_slug).exists():
            number += 1
            new_slug = "{}-{}".format(slug, number)
        slug = new_slug

        #Creates a slug from product's title.
        return slug

    def get_absolute_url(self):
        #Returns a slug with path, e.g < /product-detail/samsung-chromebook >
        return reverse('detail-product', kwargs={'slug': self.slug})

    @classmethod
    def get_product_list(cls):
        names = cls.objects.values_list('title')
        return names

    @classmethod
    def get_product(cls, slug):
        product = cls.objects.get(slug=slug)
        return product

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id
            self.slug = self.get_unique_slug()
        else:
            product = Product.objects.get(slug=self.slug)
            if product.title != self.title:  # self.title = güncellenen ancak veritabanına henüz kaydedilmemiş title, blog.title = güncellenmiş, veitabanındaki title.
                self.slug = self.get_unique_slug()
        super(Product, self).save(*args, **kwargs)