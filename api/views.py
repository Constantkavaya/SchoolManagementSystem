from courses.models import Courses
from django.shortcuts import render
from rest_framework import serializers,viewsets
from student.models import Student
from .serializer import StudentSerializer
from trainer.models import Trainer
from .serializer import TrainerSerializer
from .serializer import CoursesSerializer
 
# Create your views here.
 
class StudentViewSet(viewsets.ModelViewSet):
   queryset=Student.objects.all()
   serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
   queryset=Trainer.objects.all()
   serializer_class=TrainerSerializer


class CoursesViewSet(viewsets.ModelViewSet):
   queryset=Courses.objects.all()
   serializer_class=CoursesSerializer

