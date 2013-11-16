#encoding:utf-8
from django.db import models

# Create your models here.
class Sequence(models.models):
	'''
	序列库
	'''
	seq = models.CharField(max_length=6, unique=True)
	in_time = models.DateTimeField(auto_now_add=True)