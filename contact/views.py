from django.shortcuts import render

from shop.models import  Category


def contact(request):
    return render(request, 'menu/contact.html', {'categories': Category.objects.all()})
