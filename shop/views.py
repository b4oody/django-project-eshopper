from django.shortcuts import render


def shop(requests):
    return render(requests, 'menu/shop.html')
