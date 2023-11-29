import stripe
from django.conf import settings
from django.http import JsonResponse
from .models import Item, Order
from django.shortcuts import render


stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, id):
    item = Item.objects.get(id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/') + '?success=true',
        cancel_url=request.build_absolute_uri('/') + '?canceled=true',
    )
    return JsonResponse({'session_id': session.id})


def item_detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'detail.html', {'item': item})


def create_payment_intent(request, order_id):
    order = Order.objects.get(id=order_id)
    items = order.items.all()

    total_amount = sum([item.price for item in items])
    currency = items[0].currency


    if hasattr(order, 'discount'):
        total_amount -= order.discount.amount
    if hasattr(order, 'tax'):
        total_amount += order.tax.amount


    payment_intent = stripe.PaymentIntent.create(
        amount=int(total_amount * 100),
        currency=currency,
        payment_method_types=['card'],
    )
    return JsonResponse({'client_secret': payment_intent.client_secret})
