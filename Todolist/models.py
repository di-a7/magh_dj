from django.db import models

# Create your models here.
class Todo(models.Model):
   title = models.CharField(max_length = 20)
   description = models.TextField()
   is_completed = models.BooleanField(default= False)