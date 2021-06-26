from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

class WritersHomePage(TemplateView):
    template_name = 'writers-home.html'

class CartarescuPage(TemplateView):
    template_name = 'cartarescu.html'

class VancuPage(TemplateView):
    template_name = 'vancu.html'

class CarsteanPage(TemplateView):
    template_name = 'carstean.html'

class PlesuPage(TemplateView):
    template_name = 'plesu.html'

class LiiceanuPage(TemplateView):
    template_name = 'liiceanu.html'

class SociuPage(TemplateView):
    template_name = 'sociu.html'

class ComanPage(TemplateView):
    template_name = 'coman.html'

class PatapieviciPage(TemplateView):
    template_name = 'patapievici.html'

class PertaPage(TemplateView):
    template_name = 'perta.html'

class KomartinPage(TemplateView):
    template_name = 'komartin.html'

class BoiaPage(TemplateView):
    template_name = 'boia.html'

class ParaschivescuPage(TemplateView):
    template_name = 'paraschivescu.html'
