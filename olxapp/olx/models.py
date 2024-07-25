
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import  models


class Login(models.Model):
    username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    def __str__(self):
            return self.Username 

class User(models.Model):
    LOGIN=models.ForeignKey(Login,default='',on_delete=models.CASCADE)
    Username=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Dob=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Post=models.CharField(max_length=100)
    Pin=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    State=models.CharField(max_length=100)

    def __str__(self):
            return self.Username


class Product_view(models.Model):
    Addtitle = models.CharField(max_length=200,default='')
    Brand = models.CharField(max_length=100,default='')
    Price = models.DecimalField(max_digits=10, decimal_places=2,default='')
    Location = models.CharField(max_length=200,default='')
    Discription = models.TextField(max_length=225,default='' )
    Year = models.PositiveIntegerField(default='')
    Phone = models.CharField(max_length=15,default='',null=True, blank=True)
    Images = models.ImageField(upload_to='products/',default='')
    State = models.CharField(max_length=100,default='')
    District = models.CharField(max_length=100,default='')


    def __str__(self):
            return self.Addtitle






# class Product_sell(models.Model):
#     Fk = models.ForeignKey(Product_view, on_delete=models.CASCADE, related_name='Product_view',default='none')
#     Addtitle = models.CharField(max_length=200 ,default='')
#     Brand = models.CharField(max_length=100,default='')
#     Price = models.DecimalField(max_digits=10, decimal_places=2,default='')
#     Location = models.CharField(max_length=200,default='')
#     Discription = models.TextField(max_length=225,default='')
#     Year = models.PositiveIntegerField(default='')
#     Phone = models.CharField(max_length=15,default='')
#     Images = models.ImageField(upload_to='products/',default='')
#     State = models.CharField(max_length=100,default='')
#     District = models.CharField(max_length=100,default='')


#     def __str__(self):
#             return self.Addtitle
            

