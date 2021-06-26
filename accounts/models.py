
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

from django.db import models
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return "@{}".format(self.user.username)
        #username e built in attribute

    #def save(self,*args,**kwargs):
        #super(Profile,self).save(*args,**kwargs)

        #img = Image.open(self.image.path) #deschide poza instantei curente
        #if img.height > 250 or img.width > 250:
            #output_size = (250,250)
            #img.thumbnail(output_size)
            #img.save(self.image.path)
