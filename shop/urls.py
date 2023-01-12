from django.conf.urls.static import static
from django.urls import path, include
from eshopper_django import settings
from shop import views


urlpatterns = [
    path('', views.shop, name='shop')

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
