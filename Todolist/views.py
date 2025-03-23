from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
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

def todo(request):
   obj = Todo.objects
   todo = obj.all()
   completed =obj.filter(is_completed = True).count()
   incompleted =obj.filter(is_completed = False).count()
   context = {
      'todos' : todo,
      'completed' : completed,
      'incompleted' : incompleted
   }
   return render(request, 'todo.html',context)

def create(request):
   if request.method == "POST":
      titles = request.POST.get('title')
      descriptions = request.POST.get('description')
      if titles == "" and descriptions == "":
         context = {
            'error':"Both Title and Description are required"
         }
         return render(request, 'create.html',context)
      Todo.objects.create(title = titles, description = descriptions)
      return redirect('/todolist/')
      # return HttpResponse(description)
   return render(request,'create.html')

def mark(request,pk):
   task = Todo.objects.get(pk=pk)
   task.is_completed = True
   task.save()
   return redirect('/todolist/')

def edit(request,pk):
   task = Todo.objects.get(pk = pk)
   context = {
      "task":task
   }
   if request.method == "PUT":
      titles = request.POST.get('title')
      descriptions = request.POST.get('description')
      task.title = titles
      task.description = descriptions
      task.save()
      return redirect('/todolist/')
   return render(request,'edit.html',context)

def delete(request, pk):
   task = Todo.objects.get(pk = pk)
   task.delete()
   return redirect('/todolist/')
# PUT
# {'title':"new data",
#  'description':"previoue data"}
# # PATCH
# {'title':'new data'}