from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ view of the bag contents """

    return render(request, 'bag/bag.html')
