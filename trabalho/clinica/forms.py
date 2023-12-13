from django import forms
from .models import *

class novoEnderecoForm(forms.ModelForm):
    
    class Meta:
        model = Endereco
        fields = ('cep', 'logradouro', 'bairro', 'cidade', 'estado')