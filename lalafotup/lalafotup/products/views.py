from django.shortcuts import render

# Create your views here.
from .models import RuralGovernment, Village, Product, Category


def rural_government_page(request):
    rural_government = RuralGovernment.objects.all()
    context = {'rural_governments': rural_government}
    return render(request, 'products/rural_government.html', context)


def village_page(request, government_id):
    government = RuralGovernment.objects.get(id=government_id)
    villages = government.village_set.all()
    context = {'villages': villages}
    return render(request, 'products/village.html', context)


def product_page(request, category_id):
    category = Category.objects.get(id=category_id)
    product = category.product_set.all()
    context = {'products': product}
    return render(request, 'products/product.html', context)


def category_page(request, village_id):
    village = Village.objects.get(id=village_id)
    category = village.category_set.all()
    context = {'categories': category}
    return render(request, 'products/category.html', context)
