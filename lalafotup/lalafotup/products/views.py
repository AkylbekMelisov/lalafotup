from django.shortcuts import render

# Create your views here.
from products.models import RuralGovernment, Village


def rural_government_page(request):
    rural_government = RuralGovernment.objects.all()
    context = {'rural_governments':rural_government}
    return render(request,'products/rural_government.html',context)

def village_page(request):
    village = Village.objects.all()
    context = {'villages':village}
    return render(request,'products/village.html',context)
