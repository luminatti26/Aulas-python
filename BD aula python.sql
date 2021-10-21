create database projeto;

use projeto;

create table clientes(
nome varchar(30),
cidade varchar(30),
idade int
);
        
ALTER table clientes add email varchar(30);

alter table clientes drop email;                

rename table clientes to usuarios;

drop database projeto;

insert into clientes values("ralf", "blumenau", 23);

select * from clientes;

insert into clientes (nome, idade) values("lucas", 23);

insert into clientes values 
("mayra", "joinville", 31),
("herique", "blumenau", 30),
("paloma","florianopolis", 32);

update clientes set cidade = "joinville" where nome = "paloma";

delete from clientes where nome = "paloma";
	
select * from clientes where idade > 30;    

insert into clientes values("igor", "pomerode", 25 );

select * from clientes where idade > 30 and cidade <> "blumenau";

select * from clientes where idade > 30 or cidade <> "blumenau";

select max(idade) from clientes;

select min(idade) from clientes;

select count(*)from clientes;

select avg(idade) from clientes;

select sum(idade) from clientes;

select * from clientes where nome like "h%";

select * from clientes where nome like "%a";

select * from clientes where nome like "%r%";

select * from clientes where cidade in ("blumenau", "joinville");

select * from clientes where idade between 20 and 30;

select * from clientes order by nome asc;

select * from clientes order by nome desc;

select cidade, count(*) from clientes group by cidade;

select cidade, count(*) from clientes group by cidade order by count(*) asc;
