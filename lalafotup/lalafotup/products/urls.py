from django.urls import path
from .views import *


urlpatterns = [
    path('', rural_government_page, name='home'),
    path('villages/<int:government_id>/', village_page, name='villages'),
    path('subcategory/<int:category_id>/', sub_category, name='subcategory'),
    path('category/<int:village_id>/', category_page, name='category'),
    path('products/<int:subcategory_id>/', product_page, name='products'),
    path('create_product/<int:subcategory_id>/', create_product_page, name='create_product'),

]
