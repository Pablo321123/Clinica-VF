CREATE DATABASE cvb;
use cvb;

CREATE TABLE pessoa(
	codigo int primary key,
	nome varchar (70) not null,
	email varchar (70) not null,
	telefone varchar (70) not null,
	cep varchar (70) not null,
	logradouro varchar (70) not null,
	bairro varchar (70) not null,
	cidade varchar (70) not null,
	estado varchar (70) not null
);

CREATE TABLE Funcionario (
    datacontrato date NOT NULL,
    salario decimal(10,2) NOT NULL,
    senha varchar(20) not null,
    codigo int not null,
    primary key (codigo),
    constraint fk_funcionario_pessoa foreign key (codigo) references pessoa(codigo)
    on delete no action on update no action
);

CREATE TABLE Medico (
    especialidade varchar(40) NOT NULL,
    crm int NOT NULL,
    codigo int not null,
    primary key (codigo),
    constraint fk_medico_funcionario foreign key (codigo) references funcionario(codigo)
    on delete no action on update no action
);

CREATE TABLE Agenda (
    codigo int NOT NULL,
    codigo_pasciente int,
    data_agenda date not null,
	horario varchar(20)  not null,
	nome varchar (70) not null,
	email varchar (70) not null,
	telefone varchar (70) not null,
	codigomedico int not null,
    primary key (codigo),
    constraint fk_agenda_medico foreign key (codigomedico) references medico(codigo) on delete no action on update no action,
    constraint fk_agenda_pascinete foreign key (codigo_pasciente) references pessoa(codigo)
    on delete no action on update no action
);

CREATE TABLE Paciente (
    peso decimal(6,2) NOT NULL,
    altura decimal(6,2) NOT NULL,
    tiposanguineo varchar(3) not null,
    codigo int not null,
    primary key (codigo),
    constraint fk_paciente_pessoa foreign key (codigo) references pessoa(codigo)
    on delete no action on update no action
);

CREATE TABLE ProntuarioEletronico (
    anamnese varchar(1000),
    medicamentos varchar(100),
    atestados varchar(300),
    exames varchar(300),
    codigo_med int not null,
    codigo int not null,
    constraint fk_prontuario_paciente foreign key (codigo) references paciente(codigo)
    on delete no action on update no action,
    constraint fk_prontuario_medico foreign key (codigo_med) references Medico(codigo)
    on delete no action on update no action
);

CREATE TABLE enderecos (
	cep varchar(9) not null,
	logradouro varchar(50) not null,
	bairro varchar(40) not null,
	cidade varchar(40) not null,
	estado varchar(20) not null
);
