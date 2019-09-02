from django.urls import path
from Product.views import add_product, detail_product, delete_product, edit_product, list_product
urlpatterns = [
    path('', add_product, name='add-product'),
    path('/product-detail/<slug:slug>', detail_product, name='detail-product'),
    path('/product-delete/<slug:slug>', delete_product, name='delete-product'),
    path('/product-edit/<slug:slug>', edit_product, name='edit-product'),
    path('/products', list_product, name = 'list-products')
]
