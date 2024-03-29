from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.conf import settings
from datetime import datetime

global logado


def entrarClinica(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]
            try:
                pessoa = Pessoa.objects.get(email=email)
                print(pessoa)
            except:
                return render(request, "clinica/entrar_error.html")
            funcionario = Funcionario.objects.get(codigo=pessoa)
            if funcionario.senha == senha:
                settings.LOGADO = True
                return redirect("/novofuncionario")
            else:
                return render(request, "clinica/entrar_error.html")

    else:
        form = LoginForm()
        return render(request, "clinica/entrar.html")


def entrarError(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]
            try:
                pessoa = Pessoa.objects.get(email=email)
                print(pessoa)
            except:
                return render(request, "clinica/entrar_error.html")
            funcionario = Funcionario.objects.get(codigo=pessoa)
            if funcionario.senha == senha:
                return redirect("/novofuncionario")
            else:
                return render(request, "clinica/entrar_error.html")

    else:
        form = LoginForm()
        return render(request, "clinica/entrar.html")


def agendamentoClinica(request):
    medicos = Medico.objects.all()
    especialidade = []
    for medico in medicos:
        if medico.especialidade not in especialidade:
            especialidade.append(medico.especialidade)

    if request.method == "POST":
        form = novoAgendamentoForm(request.POST)

        if form.is_valid:
            task = form.save(commit=False)
            task.codigo = int(str(id.codigo)) + 1
            task.save()
            return redirect("/agendamentos")

    else:
        especialidade_id = request.GET.get("espec")
        medesp = Medico.objects.filter(especialidade=especialidade_id)
        form = novoAgendamentoForm()
        return render(
            request,
            "clinica/agendamento.html",
            {"especialidade": especialidade, "medesp": medesp},
        )

    """
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
    """


def indexClinica(request):
    settings.LOGADO = False
    return render(request, "clinica/index.html")


def enderecosClinica(request):
    if settings.LOGADO:
        enderecos = Endereco.objects.all().order_by("cep")
        return render(request, "clinica/enderecos.html", {"enderecos": enderecos})
    else:
        return render(request, "clinica/index.html")


def galeriaClinica(request):
    return render(request, "clinica/galeria.html")


def novoEnderecoClinica(request):
    if request.method == "POST":
        form = novoEnderecoForm(request.POST)

        if form.is_valid:
            task = form.save(commit=False)
            task.save()
            return redirect("/index")

    else:
        form = novoEnderecoForm()
        return render(request, "clinica/novoendereco.html", {"form": form})


def novoFuncionarioClinica(request):
    if settings.LOGADO:
        return render(request, "clinica/novofuncionario.html")
    else:
        return render(request, "clinica/index.html")


def novoPacienteClinica(request):
    if settings.LOGADO:
        if request.method == "POST":
            form_pessoa = novaPessoaForm(request.POST)
            form_paciente = PacienteForm(request.POST)

            if form_pessoa.is_valid() and form_paciente.is_valid():
                pessoa = form_pessoa.save()
                pessoas = Pessoa.objects.last()
                paciente = form_paciente.save(commit=False)
                paciente.codigo = pessoas
                paciente.save()
                return redirect("/index")

        else:
            form_pessoa = novaPessoaForm(request.POST)
            form_paciente = PacienteForm(request.POST)
            return render(
                request,
                "clinica/novopaciente.html",
                {"form_pessoa": form_pessoa, "form_paciente": form_paciente},
            )
        
    else:
        return render(request, "clinica/index.html")


def pacientesClinica(request):
    if settings.LOGADO:
        pacientes = Paciente.objects.all().order_by("codigo")
        return render(request, "clinica/pacientes.html", {"pacientes": pacientes})
    else:
        return render(request, "clinica/index.html")


def todosAgendamentosClinica(request):
    if settings.LOGADO:
        agendamentos = Agenda.objects.all().order_by("codigo")
        return render(
            request, "clinica/todosagendamentos.html", {"agendamentos": agendamentos}
        )
    else:
        return render(request, "clinica/index.html")


def funcionariosClinica(request):
    if settings.LOGADO:
        funcionarios = Funcionario.objects.all().order_by("codigo")
        return render(
            request, "clinica/funcionarios.html", {"funcionarios": funcionarios}
        )
    else:
        return render(request, "clinica/index.html")


def todosProntuarios(request):
    if settings.LOGADO:
        prontuarios = ProntuarioEletronico.objects.all().order_by("codigo")
        return render(request, "clinica/prontuarios.html", {"prontuarios": prontuarios})
    else:
        return render(request, "clinica/index.html")


def loadDoctor(request):

    especialidade_name = request.GET.get("espec")
    doctors_names = Medico.objects.filter(especialidade=especialidade_name)

    return render(request, "clinica/doctor_options.html", {"doctors": doctors_names})

def verifyHours(request):
    dataSelecionada_raw = request.GET.get("dataAgendamento")

    # Separando a data da parte adicional
    dataPartes = dataSelecionada_raw.split(",")
    
    # Usando apenas a primeira parte como a data
    dataSelecionada = dataPartes[0].strip()

    try:
        # Convertendo a data para o formato esperado
        dataSelecionada = datetime.strptime(dataSelecionada, "%Y-%m-%d").date()
    except ValueError:
        return HttpResponse("Formato de data inválido")

    codDoctor = request.GET.get("codigo")    
    print(codDoctor)
    
    consultasAgendadas = Agenda.objects.filter(data_agenda=dataSelecionada, codigomedico=codDoctor)

    # Criando uma lista para armazenar os dados no formato desejado
    agenda_list = []

    # Iterando sobre as consultas e convertendo cada objeto para um dicionário
    for agenda in consultasAgendadas:
        agenda_dict = {
            "codigo": agenda.codigo.id,
            "data_agenda": agenda.data_agenda.strftime("%Y-%m-%d"),
            "horario": agenda.horario,
            "nome": agenda.nome,
            "email": agenda.email,
            "telefone": agenda.telefone,
            "codigomedico": agenda.codigomedico,
        }
        agenda_list.append(agenda_dict)

    # Criando a resposta JSON usando JsonResponse
    response_data = {"consultasAgendadas": agenda_list}

    print(response_data)

    return JsonResponse(response_data)

def cadastrarProntuario(request):
    if settings.LOGADO:
        if request.method == "POST":
            form_pessoa = CodigoForm(request.POST)
            form_prontuario = ProntuarioEletronicoForm(request.POST)
            if form_pessoa.is_valid() and form_prontuario.is_valid():
                codigo = form_pessoa.cleaned_data["nome"]
                pessoa = Pessoa.objects.get(codigo=codigo)
                form_prontuario.save(commit=False)
                paciente = Paciente.objects.get(codigo=pessoa)
                form_prontuario.codigo = pessoa
                return render(request, "clinica/prontuarios.html")
            return render(request, "clinica/index.html")
        else:
            form_pessoa = CodigoForm(request)
            form_prontuario = ProntuarioEletronicoForm(request)
            return render(request, "clinica/cadastrarprontuario.html")
    else:
        return render(request, "clinica/index.html")
