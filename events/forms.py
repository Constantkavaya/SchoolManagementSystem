from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Event



class CalendarRegistrationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields="__all__"
        def __init__(self,*args,**kwargs):
            super(CalendarRegistrationForm,self).__init__(*args,**kwargs)
            self.fields['start_time'].input_formats('%Y-%m-%dT%H:%M',)
            self.fields['end_time'].input_formats('%Y-%m-%dT%H:%M',)
        


        