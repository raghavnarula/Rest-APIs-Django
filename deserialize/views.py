from django.shortcuts import render
import requests
from django.http import HttpResponse

def get_things(request):
    url='http://127.0.0.1:8000/hell/'
    r=requests.get(url)
    print(type(r))
    t=r.json()
    print(type(t))
    print(t[0]['work'])
    return HttpResponse('Hello')