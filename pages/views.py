from django.shortcuts import render


def cart(request):
    return render(request, 'menu/pages/cart.html')


def checkout(request):
    return render(request, 'menu/pages/checkout.html')

