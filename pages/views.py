from django.shortcuts import render
from shop.models import Category


def cart(request):
    return render(request, 'menu/pages/cart.html', {'categories': Category.objects.all()})


def checkout(request):
    return render(request, 'menu/pages/checkout.html',{'categories': Category.objects.all()})

