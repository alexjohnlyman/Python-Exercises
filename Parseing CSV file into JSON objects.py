# This could be integrated with Stripe and/or other payment processing options

from django.shortcuts import render, render_to_response, HttpResponse
from django.template.context import RequestContext
from django.conf import settings
import stripe
import json
import csv
import os
from .models import Item


def charge_card(request):
    request_context = RequestContext(request)
    context = {'request': request}

    stripe.api_key = settings.STRIPE_API_KEY

    context['request_post'] = request.POST

    context['json_format'] = json.dumps(request.POST)

    if request.method == "POST":
        try:
            stripe_token = stripe.Token.create(
                card={
                    "number": request.POST.get('number'),
                    "exp_month": request.POST.get('month'),
                    "exp_year": request.POST.get('year'),
                    "cvc": request.POST.get('cvc')
                },
            )

            stripe_charge = stripe.Charge.create(
                amount=request.POST.get('amount'),
                currency="usd",
                source=stripe_token.get('id'),  # obtained with Stripe.js
                description="Charge for test@example.com"
            )

            context['order_status'] = "Thank you!"
        except (stripe.CardError, stripe.InvalidRequestError), e:
            context['order_status'] = e

    if request.method == "GET":
        context['order_status'] = "Please Place An Order"

    return render_to_response('index.html', context, context_instance=request_context)


def read_csv(request):
    request_context = RequestContext(request)
    context = {'request': request}

    # abspath = os.path.abspath(__file__)
    # os_path = os.path.dirname(os.path.abspath(__file__))
    # os_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # os_path3 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    #
    # print abspath
    # print os_path
    # print os_path2
    # print os_path3
    #
    # context['os_path'] = os_path
    # context['os_path2'] = os_path2
    # context['os_path3'] = os_path3
    # context['abspath'] = abspath
    #
    # context['alt_csv'] = alt_csv_file_path


    # alt_csv_file_path = "%s/csv_files/Amazon.csv" % os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    csv_file_path = "%s/Amazon.csv" % os.path.dirname(os.path.abspath(__file__))

    context['csv_path'] = csv_file_path

    csv_file = open(csv_file_path, 'r')
    line = 0
    try:
        reader = csv.reader(csv_file)
        for row in reader:
            item_id = row[0]
            title = row[1]
            description = row[2]
            manu = row[3]
            try:
                price = float(row[4])
            except:
                print "Failed converion %s %s" % (line, row[4])
                price = 0

            new_item = Item()
            new_item.item_id = item_id
            new_item.title = title
            new_item.description = description
            new_item.manufacturer = manu
            new_item.price = price
            try:
                new_item.save()
            except Exception, e:
                print e
                pass

            line = line + 1
            print line

    finally:
        csv_file.close()

    return render_to_response('csv.html', context, context_instance=request_context)


def item_list_view(request):
    request_context = RequestContext(request)
    context = {'request': request}

    items = Item.objects.all()

    context['items'] = items

    return render_to_response('item_list.html', context, context_instance=request_context)


def json_item_list(request):
    all_items = []
    json_object = {}

    items = Item.objects.all()

    item_num = 0
    for item in items:
        json_object[item_num] = {}

        json_object[item_num]['title'] = item.title
        json_object[item_num]['item_id'] = item.item_id
        json_object[item_num]['description'] = item.description
        json_object[item_num]['manufacturer'] = item.manufacturer
        json_object[item_num]['price'] = "%s" % item.price

        all_items.append(json_object[item_num])
        item_num = item_num + 1

    return HttpResponse(json.dumps(all_items))