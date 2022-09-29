import time

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from time import localtime

# Create your views here.
def exercise1(request):
    now = time.localtime()
    mon = request.GET.get('mon', now.tm_mon)
    mday = request.GET.get('mday', now.tm_mday)
    context = {'mon' : mon, 'mday' : mday}
    return render(request, 'exercise1.html', context)