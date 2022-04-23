import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project27.settings')
import django
django.setup()
import random
from faker import Faker
f=Faker()
from app.models import *
topics=['cricket','football','vollyball','kabaddi','basketball']
def add_topic():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def add_webpage(wn,wu):
    t=add_topic()
    w=Webpage.objects.get_or_create(topic_name=t,name=wn,url=wu)[0]
    w.save()
    return w
def add_accessRecord(wn,wu,wd):
    w=add_webpage(wn,wu)
    a=AccessRecords.objects.get_or_create(name=w,date=wd)[0]
    a.save()
def add_data(n):
    for i in range(1,n+1):

        wn=f.first_name()
        wu=f.url()
        wd=f.date()
        add_accessRecord(wn,wu,wd)
n=int(input('how many rows u want: '))
add_data(n)