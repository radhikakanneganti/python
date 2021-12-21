from django.db import models

# Create your models here.
from django.utils import timezone
# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    acctNumber=models.IntegerField()
    dateofactopen=models.DateTimeField()

class CustomerPurchase(models.Model):
    acctNumber=models.IntegerField()
    amount=models.FloatField()
    dateofpurchase=models.DateTimeField()