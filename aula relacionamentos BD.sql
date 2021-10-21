create database relacionamento;]

use relacionamento;

create table cidades(
	codigo int auto_increment,
    nome varchar(30),
    primary key (codigo)
    );

create table clientes (
	codigo int auto_increment,
    nome varchar(15),
    cidade int,
    primary key (codigo), 
    foreign key (cidade) references cidades(codigo)
    );



insert into cidades(nome) values
('blumenau'),
('camboriu'),
('joinville'),
('indaial');

select * from cidades;

insert into clientes(nome, cidade) values 
('Ana', 1),
('julio', 3),
('larissa', 1),
('christian', 2);

select * from clientes;

select clientes.nome, cidades.nome from clientes inner join cidades on clientes.cidade = cidades.codigo;

select cidades.nome, count(clientes.nome) from clientes left join cidades on  clientes.cidade = cidades.codigo group by cidades.nome;

select cidades.nome, clientes.nome from clientes right join cidades on clientes.cidade = cidades.codigo;
