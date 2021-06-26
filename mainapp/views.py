from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib import messages


class HomePage(TemplateView):
    template_name = 'index.html'
