use exercicios_join;

select *from clientes;

select *from cidades;

create view visao as 
select clientes.cliente, cursos.curso  from clientes inner join cursos on clientes.codigo_curso = cursos.codigo;

create view exercicio_2 as
select clientes.cliente, cursos.curso  from clientes right join cursos on clientes.codigo_curso = cursos.codigo;

create view exercicio_3 as
select count(clientes.cliente), cursos.curso from clientes right join cursos on clientes.codigo_curso = cursos.codigo group by cursos.curso;

create view exercicio_4 as
select cliente from clientes order by cliente asc;

drop view visao, exercicio_2, exercicio_3, exercicio_4;

select * from visao;
select * from exercicio_2;
select * from exercicio_3;
select * from exercicio_4;
















