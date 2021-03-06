from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    """
    This is the contents of the customers bag at any given time
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    """ For adding product into bag """
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            """
            For when adding same product into the bag
            it adjusts the quantity and price
            """
            product = get_object_or_404(Product, pk=item_id)
            for vehicle, quantity in item_data['items_by_vehicle'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'vehicle': vehicle,
                })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
