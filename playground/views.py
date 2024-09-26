from django.shortcuts import render
from django.db import transaction
from store.models import Order, OrderItem, Product, Customer, Collection



def say_hello(request):
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()
    
    return render(request, 'hello.html', {
        'name': 'Mosh',
        # 'tags': query_set
        })
