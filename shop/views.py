import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from shop.models import Category
from shop.models import Product


def shop(request):
    paginator = (Paginator(Product.objects.all(), 6))
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    page_range = paginator.get_elided_page_range(number=page)

    contex = {

        'categories': Category.objects.all(),
        'page_obj': page_obj,
        'page_range': page_range,

    }

    return render(request, 'menu/shop.html', contex)





def category(request, slug):

    paginator = Paginator(Product.objects.filter(slug=slug), 1)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    page_range = paginator.get_elided_page_range(number=page)

    context = {

        'categories': Category.objects.all(),
        'page_obj': page_obj,
        'page_range': page_range,
    }

    return render(request, 'menu/shop.html', context)










# def add_to_cart(request):
#     data = json.loads(request.body)
#     product_id = data["id"]
#     product = Product.objects.get(id=product_id)
#
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
#         cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         cartitem.amount += 1
#         print(cartitem)
#
#     return JsonResponse("it is working", safe=False)
#





# def add_to_cart(request, product_id, quantity):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.add(product, product.unit_price, quantity)
#
# def remove_from_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.remove(product)
#
#
# def get_cart(request):
#     return render(request, 'menu/pages/cart.html', {'cart': Cart(request)})