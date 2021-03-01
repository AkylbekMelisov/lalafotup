from django.urls import path
from .views import *


urlpatterns = [
    path('', rural_government_page, name='home'),
    path('villages/<int:government_id>/', village_page, name='villages'),
    path('subcategory/<int:category_id>/', sub_category, name='subcategory'),
    path('category/<int:village_id>/', category_page, name='category'),
    path('products/<int:subcategory_id>/', product_page, name='products'),
    path('create_product/<int:subcategory_id>/', create_product_page, name='create_product'),
    path('my_product/', my_product, name='my_product'),
    path('delete_product/<int:product_id>', delete_my_product, name='delete_product'),
    path('edit_product/<int:product_id>', edit_my_product, name='edit_product'),
    path('show_product/<int:product_id>/', show_product, name='show_product'),

]
