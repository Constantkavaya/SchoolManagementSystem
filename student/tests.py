

# Create your tests here.

from logging import currentframe
from django import urls
from django.http import request
from django.test import TestCase
from .models import Student
import datetime
from django .urls import reverse



class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="Linda Kay" ,last_name="Akulu",age=22,gender="Female",
        email="kay@gmail.com",phone_number="0714456789",city="Nairobi",language="English")
    def   test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())

    def  test_full_name_contains_last_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())   
    
    def  test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_student_registration_view(self):
        url= reverse("register_student")
        data={"first_name":self.student.first_name,"last_name":self.student.last_name,"age":self.student.age,"gender":self.student.gender,
        "email":self.student.email,"phone_number":self.student.phone_number,"city":self.student.city,"language":self.student.language}
        request=Self.client.past(url,data)
        Self.assertEqual(request.status_code,200)
    
    