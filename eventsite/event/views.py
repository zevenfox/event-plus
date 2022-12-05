from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime, timedelta
from django.utils.timezone import get_current_timezone

# Create your views here.

def home(request,year,month):
    name = "Micky"
    month = month.title()
    #Covert Moth from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year,month_number)
    # get_current_timezone
    now = datetime.now(get_current_timezone())
    time = now.strftime("%H:%M %d %b %Y")
    return render(request, 'home.html',{"name":name,"year":year, "month":month, "month_number":month_number, "cal":cal, "time":time})