from django.urls import path
from .views import product_list, load_data_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('load-data/', load_data_view, name='load-data'),
]