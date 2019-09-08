from django.urls import path
from Product.views import add_product, detail_product, delete_product, \
    edit_product, list_product, add_product_cart, user_cart_list, delete_cart_product

urlpatterns = [
    path('', add_product, name='add-product'),
    path('product-detail/<slug:slug>', detail_product, name='detail-product'),
    path('product-delete/<slug:slug>', delete_product, name='delete-product'),
    path('product-edit/<slug:slug>', edit_product, name='edit-product'),
    path('myCart/<slug:slug>', add_product_cart, name='add-product-cart'),
    path('myCartList/<slug:username>', user_cart_list, name='list-cart'),
    path('cart-product-delete/<int:id>', delete_cart_product, name='delete-cart-product'),
    path('products', list_product, name='list-products'),
]
