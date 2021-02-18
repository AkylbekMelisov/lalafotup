from django.urls import path
from .views import *


urlpatterns = [
    path('',rural_government_page),
    path('villages/<int:government_id>/',village_page,name='villages'),
    path('products/<int:category_id>/',product_page,name='products'),
    path('category/<int:village_id>/',category_page,name='category')
]
