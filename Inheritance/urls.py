from django.urls import path
from . import views


urlpatterns = [
  path("index/", views.index),
  path("base/", views.base),
  path("about/", views.about),
  path("footer/", views.footer),
  path("sidebar/", views.sidebar),
  path("navbar/", views.navbar),
]
  