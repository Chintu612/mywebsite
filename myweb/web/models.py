from django.db import models
from datetime import datetime,date
class Customer(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    amounttobepaid=models.IntegerField()
    def __str__ (self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=60)
    price=models.IntegerField()
    stockavailable=models.IntegerField()
    stockbought=models.IntegerField()
    def __str__ (self):
        return self.name
class Buy(models.Model):
    customer=models.ForeignKey(Customer,on_delete = models.CASCADE)
    product=models.ForeignKey(Product,on_delete = models.CASCADE)
    date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField()
    time=models.TimeField(auto_now_add=True)
    def __str__ (self):
        return self.customer.name+'--'+(str)(self.date)
  
     
            
        


