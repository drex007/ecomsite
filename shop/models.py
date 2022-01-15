from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length= 200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=350)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return  self.title

class Cart(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


    def __str__(self):
        return self.product.title


class Order(models.Model):
    items = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    total_price = models.IntegerField()
    date_of_order = models.DateTimeField(auto_now =True)
  
    def __str__(self):
        return   self.name + "Order"
   
        
        