from django.contrib import admin
from .models import Todo
# Register your models here.
# @admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
   list_display = ("title","is_completed",)
   list_filter = ("title","is_completed",)
   list_per_page = 5
   search_fields = ("title",)
   list_editable =("is_completed",)

admin.site.register(Todo, TodoAdmin)
