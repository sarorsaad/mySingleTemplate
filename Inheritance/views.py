from django.shortcuts import render

def index(request):

  return render  (request, "Inheritance/index.html")

def base(request):

  return render  (request, "Inheritance/base.html")