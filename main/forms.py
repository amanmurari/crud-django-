from django import forms
from .models import Crud_Model

class Crud_form(forms.ModelForm):
  class Meta:
    model=Crud_Model
    fields=["name","email","age","city"]
    widgets={
      "name":forms.TextInput(attrs={"id":"sname"}),
      "email":forms.EmailInput(attrs={"id":"semail"}),
      "age":forms.NumberInput(attrs={"id":"sage"}),
      "city":forms.TextInput(attrs={"id":"scity"}),
    }