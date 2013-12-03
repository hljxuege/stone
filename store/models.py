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
GOODTYPE = (
    ('FOOD', '食品'),
    ('DAILY', '日用品'),
    ('DRINGK', '饮料'),
    )
class GoodType(models.Model):
    '''
    good is type
    '''
    name = models.CharField(max_length=30, choices=GOODTYPE)
    goods = models.ManyToManyField('Good', through='GoodTypeGoods')
    in_time = models.DateTimeField(auto_now_add=True)

class GoodTypeGoods(models.Model):
    '''
    goods and good type relations
    '''
    goodtype = models.ForeignKey('GoodType', related_name='+')
    good = models.ForeignKey('Good', related_name='+')
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
    belong_type = models.CharField(max_length=22, choices=GOODTYPE)#所属类别

class GoodProfile(models.Model):
    '''
    good extra profile
    '''
    good = models.ForeignKey('Good', related_name='+')
    key1 = models.CharField(max_length=30, blank=True)
    val1 = models.CharField(max_length=30, blank=True)
    key2 = models.CharField(max_length=30, blank=True)
    val2 = models.CharField(max_length=30, blank=True)
    key3 = models.CharField(max_length=30, blank=True)
    val3 = models.CharField(max_length=30, blank=True)
    key4 = models.CharField(max_length=30, blank=True)
    val4 = models.CharField(max_length=30, blank=True)
    key5 = models.CharField(max_length=30, blank=True)
    val5 = models.CharField(max_length=30, blank=True)
    key6 = models.CharField(max_length=30, blank=True)
    val6 = models.CharField(max_length=30, blank=True)
    key7 = models.CharField(max_length=30, blank=True)
    val7 = models.CharField(max_length=30, blank=True)
    key8 = models.CharField(max_length=30, blank=True)
    val8 = models.CharField(max_length=30, blank=True)
    key9 = models.CharField(max_length=30, blank=True)
    val9 = models.CharField(max_length=30, blank=True)
    key0 = models.CharField(max_length=30, blank=True)
    val0 = models.CharField(max_length=30, blank=True)
 