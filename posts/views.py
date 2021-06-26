#POSTS VIEWS.PY
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #STIM CA CINEVA TRB SA FIE LOGAT CA SA FACA ACTIUNI -> CREARE DE UN NOU POST
from django.urls import reverse_lazy #DACA CINEVA VREA SA STEARGA POSTUL + REDIRECTIONARE
from django.views import generic
from django.http import Http404
from django.contrib import messages
from groups.models import Group,GroupMember
from braces.views import SelectRelatedMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.models import Post

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()


#CAND SELECTEZ O PERSOANA POT VEDEA O LISTA CU TOATE POSTURILE LOR
#CADN SELECTEZ UN GRUP POT VEDEA TOATE POSTARILE DIN ACEL GRUP
class PostList(SelectRelatedMixin,generic.ListView):
    #CONECTEZ LA UN MODEL
    model = models.Post
    #select_related -> NE PERMITE SA AVEM O TUPLA CU TOATE MODELELE LA CARE FACEM REFERINTA -> PRACTIC FOREIGN KEYS
    select_related = ('user','group')

#
class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
            #prefetch_related -> RECUPEREAZA AUTOMAT, INTR-UN SINGUR LOT, OBIECTELE RELATED, IN CAZUL NOSTRU CU posts
            #username__iexact -> CAS INSENSITIVE MATCH;
            #EX: username__iexact = 'username' -> VA FI MATCH SI PENTRU USERNAME, Username sau alte combinatii de litere
        except User.DoesNotExist: #DoesNotExist - atribut
            raise Http404
        else:
            return self.post_user.posts.all()


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('message','group')
    model = models.Post

    def form_valid(self, form):
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            messages.success(self.request, 'Ai postat cu succes în grup!')
            return super().form_valid(form)
        

    def get_queryset(self):
            return Group.objects.filter(group=self.request.user)


class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all') #DUPA CE STERG UN POST MA REDIRECTIONEAZA LA CELELALTE POSTURI

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'AI ȘTERS POSTAREA')
        return super().delete(*args,**kwargs)
