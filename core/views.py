from django.http import request
from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses

# Create your views here.

def home(request):
    students=Student.objects.count()
    trainer=Trainer.objects.count()
    courses=Courses.objects.count()

    data={"student":students,"trainer":trainer,"courses":courses}
    return render(request,"homepage.html",data)