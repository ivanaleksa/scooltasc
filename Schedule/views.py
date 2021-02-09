from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Schedule


def index(request):
    klas = Schedule.objects.all()
    return render(request, 'schedule.html', {"klas": klas})


def DetailSchedule(request, schedule_id):
    try:
        a = Schedule.objects.get(id=schedule_id)
    except:
        raise Http404("Такого нет :(")
    return render(request, 'scheduleDetail.html', {'schedule': a})
