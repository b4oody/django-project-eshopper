from django.core.paginator import Paginator
from django.shortcuts import render

from shop.models import Category, Product, Color


def detail_product(request, id, slug):



    context = {
        'products': Product.objects.filter(slug=slug, id=id),
        'categories': Category.objects.all(),



    }

    return render(request, 'menu/detail.html', context)



