
import events
from events.models import Event
from .utilis import Event
from calendar import day_name
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utilis import Calendar
from events.forms import CalendarRegistrationForm

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calender.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        events = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_events = events.formatmonth(withyear=True)
        context['calender'] = mark_safe(html_events)
        return context
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return day_name(year, month, day=1)
    return datetime.today()

def calender(request):
    if request.method == "POST":
        form=CalendarRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
                print(form.errors)
    else:
        form=CalendarRegistrationForm()
    return render(request,"calender.html",{"form":form})