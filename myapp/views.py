from threading import local
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
  context={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
  return render  (request, "myapp/index.html",context)

def function(request):
  return render  (request, "myapp/function.html")

def navbar(request):
  return render  (request, "myapp/navbar.html")

def calclusTXT(request):
  return render  (request, "myapp/calclusTXT.html")
def linearAlgebra(request):
  return render  (request, "myapp/linearAlgebra.html")
def cfe(request):
  return render  (request, "myapp/cfe.html")
def home(request):
    now=datetime.datetime.now()
    context={
        'first_name':'saror',
        'last_name' :'saad',
        'now':now
    }
    return render  (request, "myapp/home.html",context)
    
# def index(request):
#         now=datetime.datetime.now()
    
#         first_name='saror'
#         last_name ='saad'
    

#         return render  (request, "myapp/index.html",local())

def context(request):
    now = datetime.datetime.now()
    
    person= {'firstname': 'saror', 'lastname': 'saad'}
    item_list = {"Chocolate": 4, "Pen": 10, "Pencil": 3}
    order_number= "000132342"
    context= {
        'person': person,
        'item_list': item_list,
        'order_number': order_number,
        'current_date': now.date(),
        }
    return render(request, 'context.html', context)