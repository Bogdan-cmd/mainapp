#DE FIECARE DATA CAND UN USER SE INREGISTREAZA I SE CREEAZA PROFILUL AUTOMAT
#FARA SA MAI TREBUIASCA SA PUN EU DIN ADMIN

from django.db.models.signals import post_save, pre_delete #Se apeleaza dupa ce un user este creat
from django.contrib.auth.models import User #senderul - se trimite semnalul
from django.dispatch import receiver #o fct care preia signalul si performeaza anumite taskuri pe baza acestuia
from .models import Profile
from django.db.models import signals
#SIGNALS se importa in apps cu fct ready

#Cand un user este salvat, trimite semnalul, semnalul va fi receptionat de acel receiver si receiverul e functia
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get_or_create(user=instance)
