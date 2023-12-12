from django.shortcuts import render
from django.http import HttpResponse

def entrarClinica(request):
    return render(request, 'clinica/entrar.html')

def agendamentoClinica(request):
    return render(request, 'clinica/agendamento.html')

def indexClinica(request):
    return render(request, 'clinica/index.html')
    
def enderecosClinica(request):
    return render(request, 'clinica/enderecos.html')

def galeriaClinica(request):
    return render(request, 'clinica/galeria.html')

def novoEnderecoClinica(request):
    return render(request, 'clinica/novoendereco.html')

def novoFuncionarioClinica(request):
    return render(request, 'clinica/novofuncionario.html')

def novoPacienteClinica(request):
    return render(request, 'clinica/novopaciente.html')

def pacientesClinica(request):
    return render(request, 'clinica/pacientes.html')

def todosAgendamentosClinica(request):
    return render(request, 'clinica/todosagendamentos.html')
