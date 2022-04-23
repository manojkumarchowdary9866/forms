from pydoc_data.topics import topics
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        #print(request.POST)
        #TN=request.POST['topic']
        TN=request.POST.get('topic')
        print(TN)
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        return HttpResponse('Topic data is inserted Successfully')
    return render(request,'insert_topic.html')
def webpage(request):
    Topics=Topic.objects.all()
    d={"ts":Topics}
    if request.method=='POST':
        TN=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        #print(request.POST)
        #TN=request.POST['topic']
        WN=request.POST['name']
        WU=request.POST['url']
        W=Webpage.objects.get_or_create(topic_name=T,name=WN,url=WU)[0]
        W.save()
        return HttpResponse('Topic data is inserted Successfully')
    return render(request,'webpage.html',d)
def insert_access(request):
    Topics=Topic.objects.all()
    d={"ts":Topics}
    if request.method=='POST':
        TN=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        #print(request.POST)
        #TN=request.POST['topic']
        WN=request.POST['name']
        WU=request.POST['url']
        DD=request.POST['date']
        W=Webpage.objects.get_or_create(topic_name=T,name=WN,url=WU)[0]
        W.save()
        D=AccessRecords.objects.get_or_create(name=W, date=DD)[0]
        D.save()
        return HttpResponse('Topic data is inserted Successfully')
    return render(request,'insert_access.html',d)

# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()

    d={'ts':topics}
    return render(request,'display_topic.html',d)



def display_webpage(request):
    webpages=Webpage.objects.all()
    d={'ws':webpages}
    return render(request,'display_webpage.html',d)


def display_access(request):
    access=AccessRecords.objects.all()
    d={'ac':access}
    return render(request,'display_access.html',d)

