from django.shortcuts import render, redirect
from .models import *
from .forms import *

def entrarClinica(request):
    return render(request, 'clinica/entrar.html')

def agendamentoClinica(request):
    medicos = Medico.objects.all()
    ids = Agenda.objects.all()
    for id in ids:
        id = ids
    
    if request.method == 'POST':    
        form = novoAgendamentoForm(request.POST)

        if form.is_valid:
            task = form.save(commit=False)
            task.codigo = int(str(id.codigo)) + 1
            task.save()
            return redirect('/todosagendamentos')

    else:
        form = novoAgendamentoForm()
        return render(request, 'clinica/agendamento.html', {'medicos':medicos})

def indexClinica(request):
    return render(request, 'clinica/index.html')
    
def enderecosClinica(request):
    return render(request, 'clinica/enderecos.html')

def galeriaClinica(request):
    return render(request, 'clinica/galeria.html')

def novoEnderecoClinica(request):
    if request.method == 'POST':    
        form = novoEnderecoForm(request.POST)

        if form.is_valid:
            task = form.save(commit=False)
            task.save()
            return redirect('/index')

    else:
        form = novoEnderecoForm()
        return render(request, 'clinica/novoendereco.html', {'form':form})


def novoFuncionarioClinica(request):
    return render(request, 'clinica/novofuncionario.html')

def novoPacienteClinica(request):
    return render(request, 'clinica/novopaciente.html')

def pacientesClinica(request):
    return render(request, 'clinica/pacientes.html')

def todosAgendamentosClinica(request):
    return render(request, 'clinica/todosagendamentos.html')

def funcionariosClinica(request):
    return render(request, 'clinica/funcionarios.html')
