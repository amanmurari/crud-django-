from django.contrib import admin
from .models import Crud_Model
# Register your models here.

@admin.register(Crud_Model)
class CrudAdmin(admin.ModelAdmin):
  list_display=["name","email","age","city"]