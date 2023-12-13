from django import forms
from django.forms.models import inlineformset_factory
from .models import *

class novoEnderecoForm(forms.ModelForm):
    
    class Meta:
        model = Endereco
        fields = ('cep', 'logradouro', 'bairro', 'cidade', 'estado')

class novoAgendamentoForm(forms.ModelForm):
    
    class Meta:
        model = Agenda
        fields = ('data_agenda', 'horario', 'nome', 'email', 'telefone', 'codigomedico')
    
class novaPessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'email', 'telefone', 'cep', 'logradouro', 'bairro', 'cidade', 'estado')

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('peso', 'altura', 'tiposanguineo')

class LoginForm(forms.ModelForm):
    email=forms.CharField()
    senha=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ('email', 'senha')

    