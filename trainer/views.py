from.forms import TrainerRegistrationForm
from django.shortcuts import render

# Create your views here.

def register_trainer(request):
    form=TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})
    

def register_trainer(request):
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TrainerRegistrationForm()  
    return render(request,"register_trainer.html",{"form":form})     

