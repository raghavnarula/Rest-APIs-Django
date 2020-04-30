from rest_framework import serializers
from .models import FirstAttempt

class Hello(serializers.ModelSerializer):
    class Meta:
        model=FirstAttempt
        fields=['id','work','time','completed']
