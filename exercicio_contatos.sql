create database contatos;

use contatos;

create table lista_de_contatos(
id int auto_increment,
nome varchar (40),
sobrenome varchar (40),
cpf varchar (11) unique,
email varchar (40),
telefone varchar (15),
primary key(id)
);

select * from lista_de_contatos;

INSERT INTO lista_de_contatos (nome, sobrenome, cpf, email, telefone) VALUES ('Lucas', 'Minatti','11575296900', 'lucas.minatti26@gmail.com', '47997068186');

delete from lista_de_contatos where id = 1;
