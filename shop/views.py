from django.core.paginator import Paginator
from django.shortcuts import render
from shop.models import Category
from shop.models import Product


def shop(request):
    paginator = Paginator(Product.objects.all().order_by(), 6)
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

    paginator = Paginator(Product.objects.filter(slug=slug).order_by(), 1)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    page_range = paginator.get_elided_page_range(number=page)

    context = {

        'categories': Category.objects.all(),
        'page_obj': page_obj,
        'page_range': page_range,
    }

    return render(request, 'menu/shop.html', context)






