from django.urls import path
from .views import *


urlpatterns = [
    path('',rural_government_page),
    path('villages/',village_page)
]
