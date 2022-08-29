from django.shortcuts import render

# Create your views here.
def index(request):
  return render  (request, "myapp/index.html")

def function(request):
  return render  (request, "myapp/function.html")

def navbar(request):
  return render  (request, "myapp/navbar.html")

def calclusTXT(request):
  return render  (request, "myapp/calclusTXT.html")
def linearAlgebra(request):
  return render  (request, "myapp/linearAlgebra.html")
# def calclusTXT(request):
#   return render  (request, "myapp/calclusTXT.html")
