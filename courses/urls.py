from django.urls import path
from.views import register_courses
from django.conf import settings
from django.conf import urls
from django.conf.urls import url
from django.conf.urls.static import static
from.views import courses_list

urlpatterns=[
    path("register/",register_courses,name="register_courses"),
    path("list/",courses_list,name="courses_list"),

]