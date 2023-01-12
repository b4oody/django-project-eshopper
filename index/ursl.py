from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from eshopper_django import settings
from index import views


urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', include('shop.urls')),
    path('detail/', include('detail.urls')),
    path('cart/', include('pages.urls')),
    path('checkout/', include('pages.urls')),
    path('contact/', include('contact.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
