from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from.models import New


class NewView(View):
    def get(self, request):
        news = New.objects.order_by('-date')
        return render(request, 'index.html', {'newlist': news})


class NewDetail(View):
    def get(self, request, pk):
        new = New.objects.get(id=pk)
        return render(request, 'newdetail.html', {'new': new})
