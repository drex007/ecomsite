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

   
        
        