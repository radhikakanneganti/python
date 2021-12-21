from rest_framework import serializers
from .models import Customer
from .models import CustomerPurchase

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['name','city','acctNumber','dateofactopen']

class CustomerPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerPurchase
        fields=['acctNumber','amount','dateofpurchase']