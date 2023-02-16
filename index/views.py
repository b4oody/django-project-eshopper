from django.shortcuts import render
from shop.models import Category


def index(request):
    return render(request, 'menu/index.html', {'categories': Category.objects.all()})


