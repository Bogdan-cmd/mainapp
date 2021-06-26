from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
# Create your models here.

import misaka


from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    #PRIN auto_now CAND UN USER POSTEAZA CEVA APARE AUTOMAT SI ORA - SE AUTOGENEREAZA
    message = models.TextField(verbose_name='Titlu')
    #CARE E MESAJUL DIN POST
    message_html = models.TextField(editable=False) #NU VREAU CA USERII SA EDITEZE POSTURILE
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=False,on_delete=models.CASCADE, verbose_name="Grup")


    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,
                                              'pk':self.pk})


    class Meta():
        ordering = ['-created_at']
        unique_together = ['user','message'] #FIECARE MESAJ ESTE LINKUIT UNIQUE CU UN USER
