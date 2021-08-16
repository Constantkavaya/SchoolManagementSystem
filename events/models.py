from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Events(models.Model):
    
 title=models.CharField(max_length=12)
 event_description=models.CharField(max_length=12)
 date=models.DateField()
 event_venue=models.CharField(max_length=15)
 event_link=models.URLField()
 attendees=models.CharField(max_length=18)
 total_attendees=models.PositiveSmallIntegerField()
 start_time=models.CharField(max_length=10)
 end_time=models.CharField(max_length=10)