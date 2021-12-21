from django.contrib import admin

from .models import Customer
from .models import CustomerPurchase

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['name','city','acctNumber','dateofactopen']

@admin.register(CustomerPurchase)
class CustomerPurchaseAdmin(admin.ModelAdmin):
    list_display=['amount','acctNumber','dateofpurchase']

