from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='productsListUrl'),#присваиваем ссылке имя для редиректа
]