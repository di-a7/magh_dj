from django.urls import path
from .views import *
urlpatterns = [
   path('home/',home),
   path('index/',index),
   path('todolist/',todo),
   path('create/',create),
   path('todolist/<pk>/',mark),
   path('todolist/<pk>/edit/',edit),
   path('todolist/<pk>/delete/',delete)
]