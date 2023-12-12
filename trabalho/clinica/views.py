from django.shortcuts import render
from django.http import HttpResponse

def entrarClinica(request):
    return render(request, 'clinica/entrar.html')