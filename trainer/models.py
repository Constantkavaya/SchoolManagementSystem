from django.db import models

# Create your models here.

class Trainer(models.Model):

 first_name=models.CharField(max_length=12)
 last_name=models.CharField(max_length=12)
 gender_choice=(( u'F',u'Female'),( u'M',u'Male'),( u'O',u'Others'))
 gender=models.CharField(max_length=10,choices=gender_choice)
 image=models.ImageField(upload_to="images")
 phone_number=models.CharField(max_length=13)
 email_address=models.EmailField()
 identification_card=models.CharField(max_length=14)
 nationality=models.CharField(max_length=15)
 languages=(( u'E',u'English'),( u'K',u'Kiswahili'),( u'F',u'French'))
 language=models.CharField(max_length=18,choices=languages)
 resume=models.FileField()
 course=models.CharField(max_length=18)
 job_title=models.CharField(max_length=20)
 days=models.CharField(max_length=15)
 company=models.CharField(max_length=25)
 salary=models.FloatField()
 contract=models.FileField()
