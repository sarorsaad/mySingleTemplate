from django.shortcuts import render

def index(request):

  return render  (request, "Inheritance/index.html")

def base(request):

  return render  (request, "Inheritance/base.html")

def about(request):
  x={
    'name':'saror','age':13
  }

  return render  (request, "Inheritance/about.html",x)

def footer(request):

  return render  (request, "Inheritance/footer.html")
def sidebar(request):

  return render  (request, "Inheritance/sidebar.html")
def navbar(request):

  return render  (request, "Inheritance/navbar.html")