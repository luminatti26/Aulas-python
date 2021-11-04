create database Projeto_1;

use projeto_1;

create table Clientes(
id int auto_increment,
nome varchar (40),
sobrenome varchar (40),
cpf varchar (11) unique,
telefone varchar (15),
primary key(id)
);

create table animais(
id int auto_increment,
nome varchar(30),
especie varchar(10) not null,
raca varchar(30),
idade int,
condicoes varchar(100),
primary key(id)
);


select * from projeto_1.clientes;
select * from projeto_1.animais;

drop table pets;