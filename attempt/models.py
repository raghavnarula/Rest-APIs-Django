from django.db import models


class FirstAttempt(models.Model):
    work=models.CharField( max_length=50)
    time=models.DateField( auto_now=False, auto_now_add=False)
    completed=models.BooleanField()
    def __str__(self):
        return self.work
    


# 1 todo task ke liye we have a work time completed or not
