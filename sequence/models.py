#encoding:utf-8
from django.db import models

# Create your models here.
class Sequence(models.Model):
    '''
    序列库
    '''
    pre = models.CharField(max_length=1, blank=True)
    digest = models.CharField(max_length=5, blank=True)
    seq = models.CharField(max_length=6, unique=True, blank=True)
    in_time = models.DateTimeField(auto_now_add=True)

class SEQAdmin(Sequence):
    '''
    pass
    '''

class SEQSys(Sequence):
    '''
    pass
    '''	
class SEQMerchant(Sequence):
    '''
    pass
    '''			
class SEQEmploy(Sequence):
    '''
    pass
    '''             