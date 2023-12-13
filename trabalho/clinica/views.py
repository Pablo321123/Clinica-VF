from django.shortcuts import render, redirect
from .models import *
from .forms import *

def entrarClinica(request):
    return render(request, 'clinica/entrar.html')

def agendamentoClinica(request):
    medicos = Medico.objects.all()
    especialidade = []
    for medico in medicos:
        if medico.especialidade not in especialidade:
            especialidade.append(medico.especialidade)
    print(especialidade)

    
    if request.method == 'POST':    
        form = novoAgendamentoForm(request.POST)

        if form.is_valid:
            task = form.save(commit=False)
            task.codigo = int(str(id.codigo)) + 1
            task.save()
            return redirect('/agendamentos')

    else:
        especialidade_id = request.GET.get('espec')
        print(especialidade_id)
        medesp = Medico.objects.filter(especialidade=especialidade_id)
        print(medesp)
        form = novoAgendamentoForm()
        return render(request, 'clinica/agendamento.html', {'especialidade':especialidade, 'medesp': medesp})
    
    '''
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
            return redirect('/agendamentos')

    else:
        form = novoAgendamentoForm()
        return render(request, 'clinica/agendamento.html', {'medicos':medicos})
    '''
def indexClinica(request):
    return render(request, 'clinica/index.html')
    
def enderecosClinica(request):
    enderecos = Endereco.objects.all().order_by('cep')
    return render(request, 'clinica/enderecos.html', {'enderecos':enderecos})

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
    if request.method == 'POST':
        form_pessoa = novaPessoaForm(request.POST)
        form_paciente = PacienteForm(request.POST)

        if form_pessoa.is_valid() and form_paciente.is_valid():
            pessoa = form_pessoa.save()
            pessoas = Pessoa.objects.last()
            paciente = form_paciente.save(commit=False)
            paciente.codigo = pessoas
            paciente.save()
            return redirect('/index')

    else:
        form_pessoa = novaPessoaForm(request.POST)
        form_paciente = PacienteForm(request.POST)
        return render(request, 'clinica/novopaciente.html', {'form_pessoa': form_pessoa, 'form_paciente': form_paciente})
    
def pacientesClinica(request):
    pacientes = Paciente.objects.all().order_by('codigo')
    return render(request, 'clinica/pacientes.html', {'pacientes': pacientes})

def todosAgendamentosClinica(request):
    agendamentos = Agenda.objects.all().order_by('codigo')
    return render(request, 'clinica/todosagendamentos.html', {'agendamentos':agendamentos})

def funcionariosClinica(request):
    funcionarios = Funcionario.objects.all().order_by('codigo')
    return render(request, 'clinica/funcionarios.html', {'funcionarios': funcionarios})
