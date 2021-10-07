from courses.models import Courses
from trainer.models import Trainer
from django.db.models.base import Model
from rest_framework import serializers
 
from student.models import Student
 
class StudentSerializer(serializers.ModelSerializer):
   class Meta:
       model=Student
       fields=("first_name","last_name", "age")

class TrainerSerializer(serializers.ModelSerializer):
   class Meta:
       model=Trainer
       fields=("first_name","last_name","gender")

class CoursesSerializer(serializers.ModelSerializer):
   class Meta:
       model=Courses
       fields=("trainer","description","code","name")