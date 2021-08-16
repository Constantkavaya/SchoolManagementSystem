
from django import forms
from django.forms.forms import Form
from django.shortcuts import render # Create your views here.
from .forms import EventsRegistrationForm


def register_events(request):
    form=EventsRegistrationForm()
    return render(request,"register_events.html",{"form":form})
    

def register_trainer(request):
    if request.method=="POST":
        form=EventsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EventsRegistrationForm()  
    return render(request,"register_events.html",{"form":form})     

