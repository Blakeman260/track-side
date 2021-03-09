from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ view of the bag contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity of specified product to shopping bag """

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

    request.session['bag'] = bag
    return redirect(redirect_url)
