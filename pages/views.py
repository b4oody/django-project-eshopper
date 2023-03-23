from django.shortcuts import render
from shop.models import Category, Product, Order, Color


# def cart(request):
#
#     if request.user.is_authenticated:
#         order, created = Order.objects.get_or_create(customer=request.user, complete=False)
#         items = order.orderitem_set.all()
#
#     else:
#         items = []
#
#     return render(request, 'menu/pages/cart.html', {'categories': Category.objects.all(), 'items':items,})


def cart(request):


    context = {
        'categories': Category.objects.all(),
    }


    return render(request, 'menu/pages/cart.html', context)


#
# def cart(request):
#
#
#
#
#
#     # if request.user.is_authenticated:
#     #     cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
#     #     items = cart.cartitems.all()
#     #
#     # else:
#     #     items = []
#     #
#     #
#     # return render(request, 'menu/pages/cart.html', {'categories': Category.objects.all(), 'items':items})
#     #


# def cart(request):
#
#
#     return render(request, 'menu/pages/cart.html', {'categories': Category.objects.all()})



def checkout(request):
    return render(request, 'menu/pages/checkout.html',{'categories': Category.objects.all()})

