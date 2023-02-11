from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from task.models import Item, Order, Discount, Tax
import stripe
from rishat_test_task.settings import API_PUBLIC_KEY, API_PRIVATE_KEY


stripe.api_key = API_PRIVATE_KEY


def buy(request, id):
    if request.method == 'GET':
        item = Item.objects.get(pk=id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.item,
                    },
                    'unit_amount': 100*item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/item/' + str(item.id),
            cancel_url='http://localhost:8000/item/' + str(item.id),
        )

        return JsonResponse({"id": session["id"]})


def item(request, id):
    template = "item.html"

    if request.method == 'GET':
        item = Item.objects.get(pk=id)
        context = {"id": item.id, "item": item.item, "price": item.price, "description": item.description, "api_public_key": API_PUBLIC_KEY}
        return render(request, template, context=context)


def buy_order(request, order_number):
    if request.method == 'GET':
        order = Order.objects.get(pk=order_number)
        items = list(order.item.values())
        line_items = []
        coupon_id = None
        tax_id = None

        if Discount.objects.filter(order=order_number).exists():
            discount = float(order.discount.discount)
            coupon_id = stripe.Coupon.create(percent_off=discount, duration="once")['id']

        if Tax.objects.filter(order=order_number).exists():
            tax = float(order.tax.tax)
            tax_id = stripe.TaxRate.create(
                display_name="Sales Tax",
                inclusive=False,
                percentage=tax,
            )['id']

        for item in items:
            data_item = {
                'price_data': {
                    'currency': 'USD',
                    'product_data': {
                        'name': item['item'],
                    },
                    'unit_amount': 100 * item['price'],
                },
                'quantity': 1,
            }
            if tax_id is not None:
                data_item.update({'tax_rates': [tax_id]})

            line_items.append(data_item)

        session = stripe.checkout.Session.create(
            line_items =  line_items,
            mode = 'payment',
            discounts=[{'coupon': coupon_id}],
            success_url = 'http://localhost:8000/order/' + str(order_number),
            cancel_url ='http://localhost:8000/order/' + str(order_number)
        )

        return JsonResponse({"id": session["id"]})


def order(request, order_number):
    template = "order.html"

    if request.method == "GET":
        items = list(Order.objects.get(pk=order_number).item.values())
        context = {"order_number": order_number, "items": items, "api_public_key": API_PUBLIC_KEY}
        return render(request, template, context)

