from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=225)

    # TO correct the name category
    class Meta:
        ordering =('name',)
        verbose_name_plural ='Categories'

    # To show the item by their name in the admin login page
    def __str__(self) :
        return self.name
    
    # creating another class of Item
class Item(models.Model):
    name= models.CharField(max_length=225)
    description =models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_image', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by =models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
   
    def __str__(self) :
        return self.name