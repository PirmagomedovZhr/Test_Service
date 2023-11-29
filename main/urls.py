from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('create-payment-intent/<int:order_id>/', views.create_payment_intent, name='create_payment_intent'),
]