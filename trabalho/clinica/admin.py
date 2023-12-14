from django.contrib import admin

from .models import *

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Agenda)