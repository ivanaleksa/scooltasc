from django.shortcuts import render
from.models import Sudent


def ListStudent(request):
    student = Sudent.objects.order_by('-balls')
    return render(request, 'listStudents.html', {'students':student})


def DetailStudent(request, id):
    stident = Sudent.objects.get(id=id)
    return render(request, 'StudentDetail.html', {'student': stident})
