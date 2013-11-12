#encoding:utf-8
from django.db import models
'''
仓库
纸张　单位(unit)　张，　规格(stand)　A4[全开]　，克数，　颜色　　　　　描述　购买时间
油墨　单位　桶，　       规格　　，　颜色　　　　　描述　购买时间
'''
# Create your models here.
class Stock(models.Model):

    IN_OR_OUT_STORE = (
        ('I', 'IN'),
        ('O', 'OUT'),
    )    
    UNIT = (
        ('Z', 'Zhang'),
        ('T', 'Tong'),
        ('O', 'Other'),
    	)
    COLOR = (
		('BGE', 'beige'),#米色
		('BLU', 'blue'),#蓝色
		('BLK', 'black'),#黑色
		('LAV', 'lavender'),#淡紫色
		('BGY', 'Blue grey'),#蓝灰色
		('LBL', 'lightblue'),#浅蓝色
		('VLT', 'violet'),#紫色
		('SKY', 'skyblue'),#天蓝色
		('WHI', 'white'),#白色
		('GRY', 'grey'),#灰色
		('NAT', 'natural'),#自然色
		('GRN', 'green'),#绿色搜索
		('LPK', 'lightpink'),#浅粉色
		('AQU', 'Aqua'),#水绿色
		('MAG', 'magenta'),#洋红色
		('TUR', 'turquoise'),#青绿色
		('PNK', 'pink'),#粉色
		('CRP', 'crystal pink'),#晶粉
		('SKN', 'sky nature'),#天蓝色
		('PLT', 'purple tulip'),#紫色
		('OLV', 'olive'),#橄榄绿
		('HBL', 'hotblue'),#亮蓝
		('FUS', 'fuchsia'),#紫红色
		('GLD', 'golden'),#金色
		('PUR', 'purple'),#紫色
		('RED', 'red'),#红色
		('SAL', 'salmon'),#鲜肉色
		('YLW', 'yellow'),#黄色
		('OTH', 'other'),#其他
        )
    in_or_out_store = models.CharField(max_length=6, choices=IN_OR_OUT_STORE)
    unit = models.CharField(choices=UNIT, max_length=6)
    color = models.CharField(choices=COLOR, max_length=6)
    name = models.CharField(max_length=6)
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=20)
    in_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

class PaperStock(Stock):   
    
    g_num = models.IntegerField()


class InkStock(Stock):
    pass
    
 
 