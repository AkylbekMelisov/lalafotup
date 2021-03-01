from django import forms
from django.contrib.auth.forms import UserCreationForm

from products.models import *

register_forms = UserCreationForm()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'phone', 'subcategory', 'description', ]
