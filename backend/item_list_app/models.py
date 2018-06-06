from django.db import models
import django.utils.timezone as timezone
import datetime
class Card(models.Model):
	cardNo=models.CharField(max_length=100)
	foundTime=models.DateField()
	keep=models.CharField(max_length=10,default='本人保管')
	status=models.CharField(max_length=10,default='未领取')
	phone=models.CharField(max_length=20)

class otherItem(models.Model):
	itemName=models.CharField(max_length=30)
	foundTime=models.DateField()
	keep=models.CharField(max_length=10,default='本人保管')
	status=models.CharField(max_length=10,default='未领取')
	phone=models.CharField(max_length=20)
	description=models.CharField(max_length=250)
