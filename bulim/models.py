
from distutils.archive_util import make_zipfile
from django.db import models
from django.contrib.auth.models import User
from PIL import Image  

class IndexXat(models.Model):
     ism = models.CharField(max_length=150, default='Nomalum', null=True)
     email = models.CharField(max_length=50, default='Nomalum', null=True)
     savol = models.TextField(max_length=1500, default='Nomalum')




class Product(models.Model):

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
 

class Foydalanuvchi(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        image = models.ImageField(default='7459.jpg',upload_to='profile_pics')   
        
         
        def __str__(self):
             return f'{self.user.username} Profile'

     
        def save(self, *args, **kwargs):
             super(Foydalanuvchi, self).save( *args, **kwargs)

             img = Image.open(self.image.path)
             
             if img.height > 300 or img.width > 300 :
                     output_size = (300,300)
                     img.thumbnail(output_size)
                     img.save(self.image.path) 
 
 