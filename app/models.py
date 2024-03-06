from django.db import models

# Create your models here.
class ProductCatagory(models.Model):
    Product_catagory_id=models.IntegerField(primary_key=True)
    Product_catagory_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Product_catagory_name

class Product(models.Model):
    Product_catagory_id=models.ForeignKey(ProductCatagory,on_delete=models.CASCADE)
    Product_id=models.IntegerField()
    Product_name=models.CharField(max_length=100)
    Product_price=models.IntegerField()
    Product_brand=models.CharField(max_length=100)
     

    def __str__(self):
        return self.Product_name

