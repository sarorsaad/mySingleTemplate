from django.urls import path
from . import views


urlpatterns = [
  path("", views.index),
  path("function/", views.function),
  path("navbar/", views.navbar),
  path("calclusTXT/", views.calclusTXT),
  path("linearAlgebra/", views.linearAlgebra),
  path("cfe/", views.cfe),
  path("index/", views.index),
  path("home/", views.home),
  path("context/", views.context),
]