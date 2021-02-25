
from django import forms
from django.contrib.auth.forms import UserCreationForm

from products.models import Product

register_forms = UserCreationForm()


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'phone', 'subcategory', 'description']
