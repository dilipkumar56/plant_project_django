from django.core import paginator
from django.shortcuts import render
from .models import Order, Products
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    product_objects = Products.objects.all()

    # sreach_code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(tittle__icontains=item_name)

    # paginator code
    paginator = Paginator(product_objects, 8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'plant_app/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'plant_app/detail.html', {'product_object': product_object})


def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        gmail = request.POST.get('gmail', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")
        order = Order(items=items, name=name, gmail=gmail,
                      address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()

    return render(request, 'plant_app/checkout.html')
