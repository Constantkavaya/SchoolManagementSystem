from datetime import datetime, timedelta
from calendar import HTMLCalendar
import events
from .models import Event
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
    def formatday(self, day, events):
         events_per_day = events.filter(start_time__day=day)
         d = ''
         for event in events_per_day:
             d += f'<li class="calendar_list"> {event.get_html_url} </li>'
             if day != 0:
                 return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
                 return '<td></td>'
    def formatweek(self, theweek, events):
         week = ''
         for d, weekday in theweek:
             week += self.formatday(d, events)
             return f'<tr> {week} </tr>'
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
        events = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'
        events += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        events += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            events += f'{self.formatweek(week, events)}\n'
            return events

