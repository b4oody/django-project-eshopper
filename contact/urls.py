from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from eshopper_django import settings
from contact import views


urlpatterns = [
    path('', views.contact, name='contact'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
