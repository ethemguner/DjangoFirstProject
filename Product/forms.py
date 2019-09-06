from django import forms
from .models import Product, Cart

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'name', 'price', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
        self.fields['description'].widget.attrs['rows'] = 10

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product']

class ProductQueryForm(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control',
                                                                           'placeholder':'search'}), required=False)
