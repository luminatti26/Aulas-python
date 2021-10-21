create database Exercicios_Join;

use Exercicios_Join;

create table cursos (
	codigo int auto_increment,
    primary key(codigo),
    curso varchar(20)
    );
    
create table clientes(
codigo int auto_increment,
primary key(codigo),
cliente varchar (30),
codigo_curso int,
foreign key (codigo_curso) references cursos(codigo)
);
    
    
insert into cursos(curso) values
('Java'),
('C#'),
('Python'),
('PHP'),
('Node.js');

select * from clientes;

insert into clientes (cliente, codigo_curso) values
('Larissa', 3),
('Gabriel', 1),
('Jean', 1),
('Gabriella', 2),
('Robson', 3),
('Isabela', 3),
('Eduardo', 2),
('Juliana', 3),
('Carlos', 2),
('Lorena', 1);

select clientes.cliente, cursos.curso from clientes right join cursos on clientes.codigo_curso = cursos.codigo;

select count(clientes.cliente), cursos.curso from clientes right join cursos on clientes.codigo_curso = cursos.codigo group by cursos.curso;












