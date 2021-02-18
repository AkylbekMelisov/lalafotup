from django.urls import path

from .views import *

urlpatterns = [
    path('registers/', register_page, name='sign_up'),
    path('login/', sign_in, name='sign_in')
]
