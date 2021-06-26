from django.urls import path
from . import views

app_name = 'writers'

urlpatterns = [
    path('',views.WritersHomePage.as_view(template_name='writers/writers-home.html'),name='all'),
    path('cartarescu/',views.CartarescuPage.as_view(template_name='writers/cartarescu.html'),name='cartarescu'),
    path('vancu/',views.VancuPage.as_view(template_name='writers/vancu.html'),name='vancu'),
    path('brumaru/',views.CarsteanPage.as_view(template_name='writers/carstean.html'),name='carstean'),
    path('plesu/',views.PlesuPage.as_view(template_name='writers/plesu.html'),name='plesu'),
    path('liiceanu/',views.LiiceanuPage.as_view(template_name='writers/liiceanu.html'),name='liiceanu'),
    path('sociu/',views.SociuPage.as_view(template_name='writers/sociu.html'),name='sociu'),
    path('coman/',views.ComanPage.as_view(template_name='writers/coman.html'),name='coman'),
    path('patapievici/',views.PatapieviciPage.as_view(template_name='writers/patapievici.html'),name='patapievici'),
    path('perta/',views.PertaPage.as_view(template_name='writers/perta.html'),name='perta'),
    path('komartin/',views.KomartinPage.as_view(template_name='writers/komartin.html'),name='komartin'),
    path('boia/',views.BoiaPage.as_view(template_name='writers/boia.html'),name='boia'),
    path('paraschivescu/',views.ParaschivescuPage.as_view(template_name='writers/paraschivescu.html'),name='paraschivescu'),
]
