from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ view of the bag contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity of specified product to shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    vehicle = None
    if 'product_vehicle' in request.POST:
        vehicle = request.POST['product_vehicle']
    bag = request.session.get('bag', {})

    if vehicle:
        if item_id in list(bag.keys()):
            if vehicle in bag[item_id]['items_by_vehicle'].keys():
                bag[item_id]['items_by_vehicle'][vehicle] += quantity
            else:
                bag[item_id]['items_by_vehicle'][vehicle] = quantity
        else:
            bag[item_id] = {'items_by_vehicle': {vehicle: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of specified product in shopping bag """

    quantity = int(request.POST.get('quantity'))
    vehicle = None
    if 'product_vehicle' in request.POST:
        vehicle = request.POST['product_vehicle']
    bag = request.session.get('bag', {})

    if vehicle:
        if quantity > 0:
            bag[item_id]['items_by_size'][vehicle] = quantity
        else:
            del bag[item_id]['items_by_size'][vehicle]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ remove specified product in shopping bag """

    try:
        vehicle = None
        if 'product_vehicle' in request.POST:
            vehicle = request.POST['product_vehicle']
        bag = request.session.get('bag', {})

        if vehicle:
            del bag[item_id]['items_by_size'][vehicle]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
