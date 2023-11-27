from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .utils import load_categories, load_products

def product_list(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'product_list.html', {'products': products})

def load_data_view(request):
    categories_data = """1:Велосипеды:None
    2:Кастрюли:4
    3:Тарелки:4
    4:Посуда для кухни:5
    5:Товары для дома:None"""

    products_data = """1:Велосипед:1:100:100.50
    2:Кастрюля 1,5л:2:50:1200
    3:Тарелка 25см:3:1000:25
    4:Кастрюля 3л:2:55:300.78"""

    # Загрузка данных
    load_categories(categories_data)
    load_products(products_data)
    return HttpResponse("Data loaded")