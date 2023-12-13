from django.db import models

class Pessoa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    telefone = models.CharField(max_length=70)
    cep = models.CharField(max_length=70)
    logradouro = models.CharField(max_length=70)
    bairro = models.CharField(max_length=70)
    cidade = models.CharField(max_length=70)
    estado = models.CharField(max_length=70)

    def __str__(self):
        return str(self.codigo) + " - " + self.nome

class Funcionario(models.Model):
    datacontrato = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    senha = models.CharField(max_length=20)
    codigo = models.OneToOneField(Pessoa, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo)

class Medico(models.Model):
    especialidade = models.CharField(max_length=40)
    crm = models.IntegerField()
    codigo = models.OneToOneField(Funcionario, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo)

class Agenda(models.Model):
    codigo = models.OneToOneField(Medico, primary_key=True, on_delete=models.CASCADE)
    data_agenda = models.DateField()
    horario = models.CharField(max_length=20)
    nome = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    telefone = models.CharField(max_length=70)
    codigomedico = models.IntegerField()

class Paciente(models.Model):
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    altura = models.DecimalField(max_digits=6, decimal_places=2)
    tiposanguineo = models.CharField(max_length=3)
    codigo = models.OneToOneField(Pessoa, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo)

class ProntuarioEletronico(models.Model):
    anamnese = models.CharField(max_length=1000)
    medicamentos = models.CharField(max_length=100)
    atestados = models.CharField(max_length=300)
    exames = models.CharField(max_length=300)
    codigo = models.OneToOneField(Paciente, primary_key=True, on_delete=models.CASCADE)

class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=20)