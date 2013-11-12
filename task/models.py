#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    ownner = models.ForeignKey(User)
    assign = models.ForeignKey(User)
    watchers = models.ForeignKey(User, through='Taskwatcher')

class Taskwatcher(models.Model):
    """docstring for Taskwatcher"""
    wathcher = models.ForeignKey(User)
    task = models.ForeignKey(Task)   
    create_time = models.DateTimeField(auto_now_add=True) 

            