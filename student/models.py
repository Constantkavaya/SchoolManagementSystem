from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Student(models.Model):

    first_name=models.CharField(max_length=12,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    gender_choice=(( u'F',u'Female'),( u'M',u'Male'),( u'O',u'Others'))
    gender=models.CharField(max_length=10,choices=gender_choice ,null=True,blank=True)
    email=models.EmailField()
    student_id=models.CharField(max_length=15,null=True,blank=True)
    phone_number=models.CharField(max_length=13,null=True,blank=True)
    student_image=models.ImageField()
    city=models.CharField(max_length=10,null=True,blank=True)
    nation=(( u'K',u'Kenya'),( u'U',u'Uganda'),( u'R',u'Rwanda'),( u'S',u'Sudan'),( u'S',u'SouthSudan'))
    nationality=models.CharField(max_length=15,choices=nation,null=True,blank=True)
    languages=(( u'E',u'English'),( u'K',u'Kiswahili'),( u'F',u'French'))
    language=models.CharField(max_length=18,choices=languages,null=True,blank=True)
    medical_report=models.FileField()
    health_records=models.FileField()
    admission_date=models.DateField(max_length=15,null=True,blank=True)
    class_name=models.CharField(max_length=10,null=True,blank=True)
    room_no=models.CharField(max_length=14,null=True,blank=True)
    guardian_phonenumber=models.CharField(max_length=15,null=True,blank=True)
    guardian_name=models.CharField(max_length=20,null=True,blank=True)
    academic_year=models.DateField()
    profile_pic=models.ImageField(upload_to="images")
   
     


