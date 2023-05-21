from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember
from django.contrib import messages
from . import models
from django.shortcuts import get_object_or_404
# Create your views here.

class CreateGroupView(LoginRequiredMixin,generic.CreateView): #DUPA CE CINEVA SE LOGHEAZA SI VREA SE CREEZE UN GRUP NOU
    fields = ('name','description')
    #NEAPARAT LA CBV TRB SA CONECTEZ CU UN MODEL
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*arg,**kwargs):
        return reverse('groups:single',kwargs={"slug":self.kwargs.get("slug")})


    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group) #CURRENT USER
        except:
            messages.warning(self.request,'Atenție, deja esțti membru în acest grup!') #POT SA DAU MESAJ LA USER -> ESTI DEJA MEMBRU IN ACEST GRUP
        else:
            messages.success(self.request,'De acum ești membru în acest grup!')

        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*arg,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership = models.GroupMember.objects.filter(
                user = self.request.user,
                group__slug = self.kwargs.get('slug')
            ).get()
        except models.GroupMember.DoesNotExist: 
            messages.warning(self.request,'Nu faci parte din acest grup!')
        else:
            membership.delete()
            messages.success(self.request,'Ai părăsit grupul cu succes!')

        return super().get(request,*args,**kwargs)
