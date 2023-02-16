from django.conf.urls.static import static
from eshopper_django import settings
from django.urls import path
from detail import views


urlpatterns = [
    path('', views.detail_product, name='detail'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
