from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Creation
import chromelogger as console

def home(request):
    context = {
        'creations': Creation.objects.all()
    }

    return render(request, 'blog/creation-blog.html', context)
    console.log('Hello')


class CreationListView(ListView):
    model = Creation
    template_name = 'blog/creation-blog.html'
    context_object_name = 'creations'
    ordering = ['-date_posted']


class CreationDetailView(DetailView):
    model = Creation

    def get_context_data(self,*args, **kwargs):
        context = super(CreationDetailView, self).get_context_data()
        stuff = get_object_or_404(Creation, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['liked'] = liked

        return context


class CreationCreateView(LoginRequiredMixin, CreateView):
    model = Creation
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Creation
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        creation = self.get_object()
        if self.request.user == creation.author:
            return True
        return False


class CreationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Creation
    success_url = '/'

    def test_func(self):
        creation = self.get_object()
        if self.request.user == creation.author:
            return True
        return False

def LikeView(request, pk):
    creation = get_object_or_404(Creation, id = request.POST.get('creation_id'))
    liked = False
    if creation.likes.filter(id=request.user.id).exists():
        creation.likes.remove(request.user)
        liked = False
    else:
        liked = True
        creation.likes.add(request.user)

    return HttpResponseRedirect(reverse('blog:detail', args=[str(pk)]))
