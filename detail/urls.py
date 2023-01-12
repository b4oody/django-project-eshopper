from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from eshopper_django import settings
from detail import views


urlpatterns = [
    path('', views.detail, name='detail'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
