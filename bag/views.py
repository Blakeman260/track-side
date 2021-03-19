from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ view of the bag contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity of specified product to shopping bag """

    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(
                    request, f'Updated {product.name} for {vehicle.upper()} quantity to {bag[item_id]["items_by_vehicle"][vehicle]}')
            else:
                bag[item_id]['items_by_vehicle'][vehicle] = quantity
                messages.success(
                    request, f'Added {product.name} for {vehicle.upper()} to your Shopping bag!')
        else:
            bag[item_id] = {'items_by_vehicle': {vehicle: quantity}}
            messages.success(
                request, f'Added {product.name} for {vehicle.upper()} to your Shopping bag!')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to your Shopping bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of specified product in shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    vehicle = None
    if 'product_vehicle' in request.POST:
        vehicle = request.POST['product_vehicle']
    bag = request.session.get('bag', {})

    if vehicle:
        if quantity > 0:
            bag[item_id]['items_by_size'][vehicle] = quantity
            messages.success(
                request, f'Updated {product.name} for {vehicle.upper()} quantity to {bag[item_id]["items_by_vehicle"][vehicle]}')
        else:
            del bag[item_id]['items_by_size'][vehicle]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f'Removed {product.name} for {vehicle.upper()} from your Shopping bag!') 
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your Shopping bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ remove specified product in shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        vehicle = None
        if 'product_vehicle' in request.POST:
            vehicle = request.POST['product_vehicle']
        bag = request.session.get('bag', {})

        if vehicle:
            del bag[item_id]['items_by_size'][vehicle]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f'Removed {product.name} for {vehicle.upper()} from your Shopping bag!')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your Shopping bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
