from django.urls import path
from .views import *

urlpatterns = [
    path('university', show_uni),
    path('addproduct', add_product,name='addproduct'),
]