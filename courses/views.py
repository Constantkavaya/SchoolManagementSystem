
from courses.forms import CoursesRegistrationForm
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Courses 




def register_courses(request):
    if request.method=="POST":
        form=CoursesRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CoursesRegistrationForm()
    return render(request,"register_courses.html",{"form":form}) 
     

def courses_list(request) :
    courses=Courses.objects.all()
    return render(request,"courses_list.html",{"courses":courses})

def edit_courses(request ,id):
    courses=Courses.objects.get(id=id)
    if request.method=="POST":
        form=CoursesRegistrationForm(request.POST,instance=courses)
        if form.is_valid():
            form.save()
    else:
        form=CoursesRegistrationForm(instance=courses)  
        return render(request ,"edit_courses.html",{"form":form}) 
   


