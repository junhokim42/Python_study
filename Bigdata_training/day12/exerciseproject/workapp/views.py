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

def exercise2(request):
    memberlist = ['Junho']
    query = 'type' in request.GET
    if query:
        if request.GET['type'] == 'memberlist':
            context = {
                'memberlist' : memberlist,
            }
        elif request.GET['type'] == 'number':
            number = len(memberlist)
            context = {
                'number': number
            }

    else:
        result = 'type = memberlist 또는 type = number로 쿼리를 전달하세요'

        context = {'result' : result}

    return render(request, 'exercise2.html', context)

def exercise3(request):
    context = None
    if request.method == 'POST':
        name = request.POST.get("name", "없음")
        opinion = request.POST.get("opinion", "없음")
        context = {
            'info': {
                'name' : name,
                'opinion': opinion,
            }
        }
    return render(request, 'exercise3.html', context)