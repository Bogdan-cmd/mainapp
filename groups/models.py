from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

import misaka

from django.contrib.auth import get_user_model
User = get_user_model() #current user sessions

from django import template
register = template.Library()
#custom template tags

class Group(models.Model):
    name = models.CharField(max_length=255,unique=True, verbose_name='Nume')
    slug = models.SlugField(allow_unicode=True,unique=True)
    #UN SLUG -> GENEREAZA UN URL VALID, CARE DE OBICEI FOLOSESTE DATE DEJA OBTINUTE
    #allow_unicode -> O INSTRUCTIUNE BOOLEANA CE INSTRUIESTE FIELDUL SA ACCEPTE UNICODE LETTERS IN DETRIMENTUL ASCII LETTERS
    #allow_unicode -> BY DEFAULT, ESTE FALSE
    description = models.TextField(blank=False,default='', verbose_name='Descriere',)
    description_html = models.TextField(editable=False,default='',blank=True)
    #IN CAZ CA VREAU O DESCRIERE HTML
    members = models.ManyToManyField(User,through='GroupMember')
    #LA ManyToManyField ESTE ASOCIAT CU argumentul through pentru a pointa inspre modelul ce se va comporta ca un intermediar
    #creator = models.OneToOneField(User,on_delete=models.CASCADE,related_name="group_creator",null=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs): #CAND VREAU SA SALVEZ UN GRUP
        self.slug = slugify(self.name) #ORICARE AR FI NUMELE, POT SA PUN SPATII SI CHESTII IN FORMULARE
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta():
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    #UN GroupMember ESTE RELATED CU UN Group -> un membru din grup poate avea un membership pt un grup
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)
    #AVEM UN user(IN LEGATURA CU LINIA 9), USERUL CURENT -> user-ul se va afla in ceva grupuri

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('group','user')
