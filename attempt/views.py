from django.shortcuts import render
from rest_framework import generics
from .serializers import Hello
from .models import FirstAttempt
class Hell(generics.ListCreateAPIView):
    queryset=FirstAttempt.objects.all()
    serializer_class=Hello
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
