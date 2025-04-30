from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path("calcular/<int:altura>/<int:peso>",views.calcular_imc, name='calcular_imc')
]