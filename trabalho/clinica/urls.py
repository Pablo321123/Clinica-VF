from django.urls import path

from . import views

urlpatterns = [
    path('', views.entrarClinica, name = 'clinica')
]
