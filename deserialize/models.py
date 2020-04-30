from django.db import models

class Receive(models.Model):
    work=models.CharField( max_length=50)
    time=models.DateField( auto_now=False, auto_now_add=False)
    completed=models.BooleanField()
