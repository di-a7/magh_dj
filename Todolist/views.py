from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return HttpResponse("Hello World")

def index(request):
   person = [
      {"name": "Alice", "age": 15},
      {"name": "Bob", "age": 5},
      {"name": "Charlie", "age": 35},
      {"name": "David", "age": 60},
      {"name": "Eve", "age": 2},
      {"name": "Frank", "age": 40},
      {"name": "Grace", "age": 33},
      {"name": "Hannah", "age": 55},
      {"name": "Isaac", "age": 56},
      {"name": "Jack", "age": 16}
]
   context = {
      'title':'index page',
      'persons':person
   }
   return render(request , 'index.html', context)
# contact and aboutus