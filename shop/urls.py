from django.conf.urls.static import static
from django.urls import path, include


from eshopper_django import settings
from shop import views



urlpatterns = [
    path('', views.shop, name='shop'),

    path('<slug:slug>/', views.category, name='category'),
    path('detail/<str:slug>/<int:id>', include('detail.urls')),
    # path('add_to_cart', views.add_to_cart, name="add")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



