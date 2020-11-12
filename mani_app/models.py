from django.db import models

# Create your models here.

class Univesity(models.Model):
    name= models.CharField(max_length=250)
    address= models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Department (models.Model):
    name= models.CharField(max_length=250)
    remarks= models.CharField(max_length=300)
    universit_id= models.ForeignKey(Univesity, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name= models.CharField(max_length=250)
    price= models.IntegerField()
    description= models.TextField(blank=True, null=True)
 

    def __str__(self):
        return self.name

class Producta(models.Model):
    name= models.CharField(max_length=250)
    price= models.IntegerField()
 

    def __str__(self):
        return self.name