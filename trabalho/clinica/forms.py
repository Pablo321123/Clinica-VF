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
    #pessoa = forms.ModelChoiceField(queryset=Pessoa.objects.all())

    class Meta:
        model = Paciente
        fields = ('peso', 'altura', 'tiposanguineo')

#PacienteFormSet = inlineformset_factory(Pessoa, Paciente, form=novoPacienteForm, fields=['peso', 'altura', 'tiposanguineo'])

    