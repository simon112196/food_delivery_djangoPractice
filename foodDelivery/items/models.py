from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255) 
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_image', null=True, blank=True)
    sold_out = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    item = models.ForeignKey(Item, related_name='item', on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name='buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='seller', on_delete=models.CASCADE)
    finished_order = models.BooleanField(default=False)
    purchase_time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.item.name
    
    