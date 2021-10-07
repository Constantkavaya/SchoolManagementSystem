from calendar import day_name
import datetime
from django.db import models
from django.urls import reverse


class Event(models.Model):
  title = models.CharField(max_length=200)
  start_time = models.DateTimeField(default=datetime.date.today)
  end_time = models.DateTimeField(default=datetime.date.today)
  day_name = models.DateTimeField(default=datetime.date.today)
  get_date= models.DateTimeField(default=datetime.date.today)


  def __str__(self):
    return self.title
  @property
  def get_date(self):
     url = reverse('event_edit', args=(self.id,))
     return f'<p>{self.title}</p><a href="{url}">edit</a>'
