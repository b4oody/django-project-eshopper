from django.urls import path, include
from django.conf.urls.static import static
from eshopper_django import settings
from authentication import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    #path('registation/', views.register, name='registration'),
    path('logout/', views.logout_user, name='logout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
