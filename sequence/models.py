#encoding:utf-8
from django.db import models

# Create your models here.
class Sequence(models.models):
	'''
	序列库
	'''
	pre = models.CharField(max_length=1)
	alpha = models.CharField(max_length=2)
	digest = models.CharField(max_length=4)
	seq = models.CharField(max_length=7, unique=True)
	in_time = models.DateTimeField(auto_now_add=True)