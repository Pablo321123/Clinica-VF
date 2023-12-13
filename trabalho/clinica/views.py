from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.conf import settings

global logado

def entrarClinica(request):
    if request.method == 'POST':    
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                pessoa = Pessoa.objects.get(email=email)
                print(pessoa)
            except:
                return render(request, 'clinica/entrar_error.html')
            funcionario = Funcionario.objects.get(codigo=pessoa)
            if funcionario.senha == senha:
                settings.LOGADO = True
                return redirect('/novofuncionario')
            else:
                return render(request, 'clinica/entrar_error.html')

    else:
        form = LoginForm()
        return render(request, 'clinica/entrar.html')

def entrarError(request):
    if request.method == 'POST':    
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                pessoa = Pessoa.objects.get(email=email)
                print(pessoa)
            except:
                return render(request, 'clinica/entrar_error.html')
            funcionario = Funcionario.objects.get(codigo=pessoa)
            if funcionario.senha == senha:
                return redirect('/novofuncionario')
            else:
                return render(request, 'clinica/entrar_error.html')

    else:
        form = LoginForm()
        return render(request, 'clinica/entrar.html')

def agendamentoClinica(request):
    medicos = Medico.objects.all()
    especialidade = []
    for medico in medicos:
        if medico.especialidade not in especialidade:
            especialidade.append(medico.especialidade)

    
    if request.method == 'POST':    
        form = novoAgendamentoForm(request.POST)

        if form.is_valid:
            task = form.save(commit=False)
            task.codigo = int(str(id.codigo)) + 1
            task.save()
            return redirect('/agendamentos')

    else:
        especialidade_id = request.GET.get('espec')
        medesp = Medico.objects.filter(especialidade=especialidade_id)
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
    settings.LOGADO = False
    return render(request, 'clinica/index.html')
    
def enderecosClinica(request):
    if settings.LOGADO:
        enderecos = Endereco.objects.all().order_by('cep')
        return render(request, 'clinica/enderecos.html', {'enderecos':enderecos})
    else:
        return render(request, 'clinica/index.html')

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
    if settings.LOGADO:
        return render(request, 'clinica/novofuncionario.html')
    else:
        return render(request, 'clinica/index.html')

def novoPacienteClinica(request):
    if settings.LOGADO:
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
    else:
        return render(request, 'clinica/index.html')
    
def pacientesClinica(request):
    if settings.LOGADO:
        pacientes = Paciente.objects.all().order_by('codigo')
        return render(request, 'clinica/pacientes.html', {'pacientes': pacientes})
    else:
        return render(request, 'clinica/index.html')

def todosAgendamentosClinica(request):
    if settings.LOGADO:
        agendamentos = Agenda.objects.all().order_by('codigo')
        return render(request, 'clinica/todosagendamentos.html', {'agendamentos':agendamentos})
    else:
        return render(request, 'clinica/index.html')

def funcionariosClinica(request):
    if settings.LOGADO:
        funcionarios = Funcionario.objects.all().order_by('codigo')
        return render(request, 'clinica/funcionarios.html', {'funcionarios': funcionarios})
    else:
        return render(request, 'clinica/index.html')

def todosProntuarios(request):
    if settings.LOGADO:
        prontuarios = ProntuarioEletronico.objects.all().order_by('codigo')
        return render(request, 'clinica/prontuarios.html', {'prontuarios': prontuarios})
    else:
        return render(request, 'clinica/index.html')