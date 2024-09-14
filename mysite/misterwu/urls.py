from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='hhh'), #与base.html中的{% url 'hhh' %}相对应
    path('user/', views.user, name='uuu'),
]