from Hadas import Login
from django.urls import path
import Hadas
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('custom', views.custom, name='custom'),
    path('home', views.home, name='home'),
]
