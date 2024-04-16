from django.shortcuts import render,redirect
from .models import Crud_Model
from .forms import Crud_form

# Create your views here.
# Add New User
def register(request):
  form = Crud_form()
  if request.method=="POST":
    data = Crud_form(request.POST)
    if data.is_valid():
      name=data.cleaned_data["name"]
      email=data.cleaned_data["email"]
      age=data.cleaned_data["age"]
      city=data.cleaned_data["city"]
      a=Crud_Model(name=name,email=email,age=age,city=city)
      a.save()
      return redirect("home")
  
  return render(request,"register.html",{"form":form})

# rendering all user in table
def home(request):
  data = Crud_Model.objects.all()
  return render(request,"index.html",{"data":data,"index":0})
  
# update exist User  
def update(request,c_id):
  if request.method=="POST":
    data=Crud_Model.objects.get(pk=c_id)
    form = Crud_form(request.POST,instance=data)
    if form.is_valid():
      form.save()
      return redirect("home")
  else:
    data=Crud_Model.objects.get(pk=c_id)
    form = Crud_form(instance=data)
    return render(request,"update.html",{"form":form})
    


# Delete exist User
def delete(request,id):
  a=Crud_Model(id=id)
  a.delete()
  return redirect("home")