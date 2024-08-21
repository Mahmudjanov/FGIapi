from django.urls import path
from.views import *



urlpatterns = [
    path('get-product/', get_product),
]