from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .models import Product, Cart
from .forms import ProductForm, ProductQueryForm
from django.contrib import messages
from django.db.models import Q

from django.http import JsonResponse
from django.template.loader import render_to_string
from .templatetags import poll_extras


def add_product(request):
    form = ProductForm()
    products = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        product = form.save(commit=False)
        product.save()
        msg = "<b>{} has added successfully!".format(product.name)
        messages.success(request, msg, extra_tags="success")
        return HttpResponseRedirect(reverse('add-product', urlconf=None))

    return render(request, 'product/add-product.html', context={'form': form, 'products': products})


def detail_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    productInfo = {'name': product.name,
                   'price': product.price,
                   'description': product.description,
                   'title': product.title,
                   'added_date': product.added_date,
                   'slug': slug,
                   'get_image': product.get_image()}

    return render(request, 'product/product-detail.html', context={'product': productInfo})


def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "GET":
        msg = "<b>{} has deleted successfully.</b>".format(product.name)
        messages.success(request, msg, extra_tags='danger')
        product.delete()
        return HttpResponseRedirect(reverse('add-product', urlconf=None))

    return render(request, 'product/add-product.html', context={'product': product})


def cart_list_amount():
    count = Cart.objects.all().count()
    context = {'pAmount': count}
    return context


def home_page(request):
    response = cart_list_amount()
    amount = response.get('pAmount')
    return render(request, 'product/home-page.html', context={'pAmount':amount})


def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = ProductForm(instance=product, data=request.POST or None, files=request.FILES or None)

    if form.is_valid():
        form.save()
        msg = "<b>{} has updated!</b>".format(product.name)
        messages.success(request, msg, extra_tags="success")
        return HttpResponseRedirect(product.get_absolute_url())

    return render(request, 'product/product-edit.html', context={'product': product, 'form': form})


def list_product(request):
    products = Product.objects.all()
    form = ProductQueryForm(data=request.GET or None)
    search = None
    if form.is_valid():
        search = form.cleaned_data.get('search', None)
        if search:
            products = products.filter(Q(title__icontains=search) | Q(name__icontains=search)).distinct()

    return render(request, 'product/product-list.html', context={'products': products, 'form':form, 'search':search})


def add_product_cart(request, slug):
    data = {'is_valid': True, 'html': '', 'count': 0}
    product = get_object_or_404(Product, slug=slug)
    cart = Cart(product=product)
    cart.save()
    html = render_to_string('product/cart/nav-cart.html', request=request)
    data.update({'html': html})
    return JsonResponse(data=data)


def cart_list(request):
    products = Cart.objects.all()
    prices = products.values('product__price')

    priceList = []
    for price in prices:
        priceList.append(price.get('product__price'))

    listPrice = sum(priceList)

    return render(request, 'product/cart/cart.html', context={'products': products, 'totalPrice': listPrice})


def delete_cart_product(request, id):
    data = {'is_valid': True, 'html': ''}
    cart = Cart.objects.get(id=id)
    cart.delete()
    html = render_to_string('product/cart/cart.html', request=request)
    data.update({'html': html})

    return JsonResponse(data=data)

def search_product(request):

    return render(request, 'product/search/searching.html', context={'result':search_result, 'search':search})