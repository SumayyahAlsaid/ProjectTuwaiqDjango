from django.db import models

# Create your models here.

class Items(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ItemDetails(models.Model):
    size=models.IntegerField(null=True)
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150)
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=1000,null=True)
    
    itemsid=models.ForeignKey(Items,on_delete=models.CASCADE)

    def __str__(self):
        return self.itemsid.name
    
class Cart(models.Model):
    Id_product=models.IntegerField(null=True)
    Id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150)
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
