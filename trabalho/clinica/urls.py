from django.urls import path

from . import views

urlpatterns = [
    path('entrar', views.entrarClinica, name = 'entrar'),
    path('entrar_error', views.entrarError, name = 'entrar_error'),
    path('agendamento', views.agendamentoClinica, name = 'agendamento'),
    path('', views.indexClinica, name = ''),
    path('index', views.indexClinica, name = 'index'),
    path('enderecos', views.enderecosClinica, name = 'enderecos'),
    path('galeria', views.galeriaClinica, name = 'galeria'),
    path('novoendereco', views.novoEnderecoClinica, name = 'novoEndereco'),
    path('novofuncionario', views.novoFuncionarioClinica, name = 'novoFuncionario'),
    path('novopaciente', views.novoPacienteClinica, name = 'novoPaciente'),
    path('pacientes', views.pacientesClinica, name = 'pacientes'),
    path('todosagendamentos', views.todosAgendamentosClinica, name = 'todosagendamentos'),
    path('funcionarios', views.funcionariosClinica, name = 'funcionarios'),
    path('prontuarios', views.todosProntuarios, name = 'prontuarios'),
    path('load_doctors/', views.loadDoctor, name = 'load_doctors')

]
