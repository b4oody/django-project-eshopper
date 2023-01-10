
from django.contrib import admin
from django.urls import path, include
from index import views


urlpatterns = [
    path('', views.main, name='index')

]
