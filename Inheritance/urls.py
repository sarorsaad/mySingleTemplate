from django.urls import path
from . import views


urlpatterns = [
  path("index/", views.index,name='index'),
  path("base/", views.base,name='base'),
  path("about/", views.about,name='about'),
  path("footer/", views.footer,name='footer'),
  path("sidebar/", views.sidebar,name='sidebar'),
  path("navbar/", views.navbar,name='navbar'),
]
  