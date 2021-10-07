
from django.urls import path
from . import views
from.views import Calendar

app_name='events'
urlpatterns = [
path("register/",views.CalendarView.as_view(),name="calender"),
path("calender/",views.calender,name='calender'),

]