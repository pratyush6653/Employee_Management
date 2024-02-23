from django.db import models

# Create your models here.
class Emp(models.Model):
   name=models.CharField(max_length=255)
   emp_Id=models.CharField(max_length=50)
   phone=models.CharField(max_length=10)
   address=models.CharField(max_length=100)
   working=models.BooleanField(default=True)
   department=models.CharField(max_length=10)
   email=models.CharField(max_length=50)



    
