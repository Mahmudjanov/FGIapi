from django.urls import path
from.views import *

urlpatterns = [
    path('get-banner/', get_banner),
    path('get-service/', get_service),
    path('get-product/', get_product),
    path("create_form/", create_form),
    path("get-contact/", contact),
]

