from django.urls import path
from.views import *

urlpatterns = [
    path('get-banner/', get_banner),
    path('get-service/', get_service),
    ]