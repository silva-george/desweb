from ast import Return
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Bem vindo ao IMC </h1>")

def calcular_imc(request, altura, peso):
    altura = altura/100.0
    response = f'Calculo do IMC {peso/(altura*altura)}'
    return HttpResponse(response)  
