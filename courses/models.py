from django.db import models

# Create your models here.
class Courses(models.Model):
 name=models.CharField(max_length=24, null=True)
 code=models.CharField(max_length=50, null=True)
 description=models.DateField(null=True)
 trainer=models.CharField(max_length=25,null=True)
 
 