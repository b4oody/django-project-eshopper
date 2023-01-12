from django.conf.urls.static import static

from django.urls import path, include
from eshopper_django import settings
from pages import views


urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('', views.checkout, name='checkout')


]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
