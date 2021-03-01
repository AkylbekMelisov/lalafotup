from django.shortcuts import render, redirect

# Create your views here.
from .filter import ProductFilter
from .forms import *
from .models import *


def rural_government_page(request):
    rural_government = RuralGovernment.objects.all()
    context = {'rural_governments': rural_government}
    return render(request, 'products/rural_government.html', context)


def village_page(request, government_id):
    government = RuralGovernment.objects.get(id=government_id)
    villages = government.village_set.all()
    context = {'villages': villages}
    return render(request, 'products/village.html', context)


def product_page(request, subcategory_id):
    subcategory = SubCategory.objects.get(id=subcategory_id)
    product = subcategory.product_set.all()
    filters = ProductFilter(request.GET, queryset=product)
    product = filters.qs
    context = {'products': product, 'sub_id': subcategory.id, 'filter': filters}
    return render(request, 'products/product.html', context)


def category_page(request, village_id):
    village = Village.objects.get(id=village_id)
    category = village.category_set.all()
    context = {'categories': category}
    return render(request, 'products/category.html', context)


def sub_category(request, category_id):
    category = Category.objects.get(id=category_id)
    subcategory = category.subcategory_set.all()
    context = {'subcategories': subcategory}
    return render(request, 'products/subcategory.html', context)


def create_product_page(request, subcategory_id):
    subcategory = SubCategory.objects.get(id=subcategory_id)
    product = subcategory.product_set.all()
    form = ProductForm(initial={'subcategory': subcategory})
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products', subcategory.id)
    context = {'products': product, 'form': form}
    return render(request, 'products/create_product.html', context)


def my_product(request):
    product = Product.objects.filter(user=request.user)
    filters = ProductFilter(request.GET, queryset=product)
    product = filters.qs
    context = {'products': product, 'filter': filters}
    return render(request, 'products/my_product.html', context)


def delete_my_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('my_product')
    context = {'products': product}
    return render(request, 'products/delete_product.html', context)


def edit_my_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('products', product.subcategory.id)
    context = {'products': product, 'form': form}
    return render(request, 'products/edit_product.html', context)


def show_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'products/show_product.html', context)
