from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    
    
    
def __str__(self) -> str:
    return f"{self.name} : {self.price}"

class Meta:
    verbose_name = 'Mart Product'
    ordaring = ['price']



    
class Payment(models.Model):
    order_type = models.CharField()
    
    
class Order(models.Model):
    order_name = models.CharField()
    order_payment_method = models.CharField()