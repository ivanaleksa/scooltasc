from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher


def listTeacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'listTeacher.html', {'teacher': teacher})

