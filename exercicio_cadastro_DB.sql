create database exercicio_cadastro_DB;

use exercicio_cadastro_DB;

create table Perfil (
	codigo int auto_increment,
	nome varchar(30),
    email varchar(30),
	cargo varchar(20),
    idade int,
    primary key(codigo)
);

select * from perfil;

drop table perfil;