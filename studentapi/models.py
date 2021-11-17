from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    remark = models.CharField(max_length=500, default='No Remark')
    admitedOn = models.DateTimeField(auto_now_add=True)


