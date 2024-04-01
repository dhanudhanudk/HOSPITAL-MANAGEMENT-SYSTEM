from django.db import models

# Create your models here.
class Appointment(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    phonenumber=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=200,null=True)
    issues=models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=40,null=True)
    class Meta:
        db_table="Appointment"


class docters(models.Model):
   id=models.CharField(max_length=100,primary_key=True)
   name=models.CharField(max_length=100,null=True)
   specialist=models.CharField(max_length=100,null=True)
   number=models.CharField(max_length=100,null=True)
   class Meta:
        db_table="docters"




    
