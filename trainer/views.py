from.forms import TrainerRegistrationForm
from django.shortcuts import render
from django .shortcuts import redirect, render 
from .models import Trainer
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

def trainer_list(request) :
    trainer=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainer":trainer})   

def edit_trainer(request ,id):
    trainer=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
    else:
        form=TrainerRegistrationForm(instance=trainer)  
        return render(request ,"edit_trainer.html",{"form":form}) 

def trainer_profile(request,id) :
    trainer =Trainer.objects.get(id=id) 
    return render(request ,"trainer_profile.html",{"trainer":trainer}) 

def delete_trainer(request,id):
    trainer =Trainer.objects.get(id=id) 
    trainer.delete()
    return redirect("trainer_list") 


 

