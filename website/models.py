from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    
    create_at = models.DateField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250) 
    
    def __str__(self):
        return self.name
        
    
class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.FileField(upload_to='gallery/', max_length=100)
       
    def __str__(self):
        return self.category.name
    
    
    
    