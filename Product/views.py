from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib import messages

#from django.http import JsonResponse
#from django.template.loader import render_to_string

def add_product(request):
    form = ProductForm()
    products = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(data=request.POST)
        product = form.save(commit=False)
        product.save()
        return HttpResponseRedirect(reverse('add-product', urlconf=None))

    return render(request, 'product/add-product.html', context={'form': form, 'products': products})


def detail_product(request, slug):
    productInfo = get_object_or_404(Product, slug=slug)
    product = {'name': productInfo.name,
               'price': productInfo.price,
               'description': productInfo.description,
               'title': productInfo.title,
               'added_date':productInfo.added_date,
               'slug':slug}
    print(productInfo.added_date)
    return render(request, 'product/product-detail.html', context={'product':product})

def delete_product(request, slug):
    #product = Product.get_product(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        product.delete()
        msg = "<b>Product has deleted successfully.</b>"
        messages.success(request, msg, extra_tags='danger')
        return HttpResponseRedirect(reverse('add-product', urlconf=None))
    return render(request, 'product/add-product.html', context={'product':product})

def home_page(request):
    return render(request, 'product/home-page.html')

def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = ProductForm(instance=product, data=request.POST or None)

    if form.is_valid():
        form.save()
        msg ="<b>{} has updated!</b>".format(product.name)
        messages.success(request, msg, extra_tags="success")
        print(product.get_absolute_url())
        return HttpResponseRedirect(product.get_absolute_url())

    return render(request, 'product/product-edit.html', context={'product':product, 'form':form})

def list_product(request):
    products = Product.objects.all()
    return render(request, 'product/product-list.html', context={'products':products})