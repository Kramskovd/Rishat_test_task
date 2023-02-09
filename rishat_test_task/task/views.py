from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from task.models import Item
import stripe

stripe.api_key = "sk_test_51MZejWJoNi7SgMkemgBuH2uKcelBmcRhwqLLMdkngAT6jHwHIe3sSANqcnXwZh5KTovhhLQHeu2K2vMKuRogBEJO00ujvkAUEw"


def buy(request, id):
    if request.method == 'GET':
        item = Item.objects.get(pk=id)
        print(item.price)
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
        context = {"id": item.id, "item": item.item, "price": item.price, "description": item.description}
        return render(request, template, context=context)

