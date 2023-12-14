from django.contrib import admin

from .models import *

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Paciente)
admin.site.register(ProntuarioEletronico)
admin.site.register(Endereco)
admin.site.register(Agenda)
admin.site.register(Medico)