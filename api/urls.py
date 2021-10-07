from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CoursesViewSet
 
 
router=routers.DefaultRouter()
router.register("students/",StudentViewSet)
router.register("trainer/",TrainerViewSet)
router.register("courses/",CoursesViewSet)
 
urlpatterns=[
   path("",include(router.urls)),
]
