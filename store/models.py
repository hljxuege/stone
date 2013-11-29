#encoding:utf-8
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
'''
            Goods
             |  
--------------------------------------------------------------
    ^            ^            ^          ^           ^
    |            |            |          |           |
DigitalGoods   FoodGoods   DailyGoods  ClothGoods  PrintGoods
'''
class GoodType(models.Model):
    '''
    good is type
    '''
    name = models.CharField(max_length=30)
    in_time = models.DateTimeField(auto_now_add=True)

class GoodTypeGoods(models.Model):
    '''
    goods and good type relations
    '''
    goodtype_id = models.ForeignKey('GoodType', related_name='+', blank=True, null=True)
    good_id = models.ForeignKey('Good', related_name='+', blank=True, null=True)
    in_time = models.DateTimeField(auto_now_add=True)

class GoodCode(models.Model):
    barcode = models.CharField(max_length=30)
    qr_code = models.CharField(max_length=512)
    innercode = models.CharField(max_length=30, unique=True)
    in_time = models.DateTimeField(auto_now_add=True)

class GoodChangeRecord(models.Model):
    innercode = models.CharField(max_length=30)
    num = models.IntegerField(max_length=11)
    is_in = models.BooleanField() #True 入， Fasle 出
    good = models.ForeignKey('Good', related_name='+', blank=True, null=True)    
    in_time = models.DateTimeField(auto_now_add=True)

class Good(models.Model):
    '''
    goods
    '''
    barcode = models.CharField(max_length=30)
    qr_code = models.CharField(max_length=512)
    innercode = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    weight = models.IntegerField(max_length=11)#单个重量 单位g
    unit = models.CharField(max_length=3) #计数单位
    quantity = models.IntegerField(max_length=11)#数量

    in_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    belong_to = models.ForeignKey(User, related_name='+', blank=True, null=True)
    belong_type = models.CharField(max_length=22)#所属类别

class PrintGood(Good):
    color = models.CharField(max_length=7)
    standard = models.CharField(max_length=32)
    desc = models.CharField(max_length=512)

class PaperPrintGood(PrintGood):
    pass

class InkPrintGood(PrintGood):
    pass 

# class Stock(models.Model):

#     in_or_out_store = models.CharField(max_length=6, choices=IN_OR_OUT_STORE)
#     unit = models.CharField(choices=UNIT, max_length=6)
#     color = models.CharField(choices=COLOR, max_length=6)
#     name = models.CharField(max_length=6)
#     price = models.FloatField(default=0.0)
#     description = models.CharField(max_length=20)
#     in_time = models.DateTimeField(auto_now_add=True)
#     modify_time = models.DateTimeField(auto_now=True)

 
 