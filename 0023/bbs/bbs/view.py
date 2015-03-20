# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime
import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from message.models import message
import random
import datetime
#@csrf_exempt

def hello(request):
    return HttpResponse(r"hello world")


def time(request,span):
    span=int(span)
    t=datetime.datetime.now()+datetime.timedelta(hours=span)
    dicts=dict()
    dicts["time"]=t
    dicts["offset"]=span
    return render_to_response("time.html",dicts)



def meta(request):
    if request.method == 'GET':
        ua=request.META['HTTP_USER_AGENT']
        addr= request.META['REMOTE_ADDR']
        return render_to_response("meta.html",{'ua':ua,'addr':addr})


def bbs(request):
    list= getlist()
    return render_to_response("message.html",{'list':list})

def addmessage(request):
    if request.method =='POST':
        #req = simplejson.loads(request.raw_post_data)
        #re=csrf(request)
        name=str(request.POST.get('name'))
        message=str(request.POST.get('message'))
        savemessage(name,message)
        return HttpResponse(simplejson.dumps({'tip':'fuck you'}), content_type="application/json")

def getmessagelist(request):
    if request.method == 'POST':
        list=getlist()
        #re=csrf(request)
        if len(list)==0:
            list=[]
        return HttpResponse(simplejson.dumps(list), content_type="application/json")

def savemessage(name='user',info='nothing'):
    t=datetime.datetime.now()
    item=message(random.randint(10000,20000),name,info,t)
    item.save()

def getlist():
    list=message.objects.order_by('time')[0:10]
    return list