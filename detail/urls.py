from django.conf.urls.static import static
from django.urls import path


from eshopper_django import settings
from detail import views


urlpatterns = [
    path('', views.detail_product, name='detail'),



]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
