from django.db import models

# Create your models here.

class Crud_Model(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField(max_length=150)
  age=models.IntegerField()
  city=models.CharField(max_length=70)
  
"""  def clean(self):
    cleaned_data=super().clean()
    name_field=cleaned_data["name"]
    email_field=cleaned_data["email"]
    city_field=cleaned_data["city"]
    if (len(name_field)<5 and len(name_field)>100):
      raise ValidationError("Name is must be range in 5 to 100")
    if len(email_field)<5 and len(email_field)>100:
      raise ValidationError("Email is must be range in 5 to 100")
    if len(city_field)>70:
      raise ValidationError("City is must be 70 charcter")"""
