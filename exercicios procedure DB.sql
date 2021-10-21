create database exercicios_procedure;

use exercicios_procedure;

create table grupinho (
	codigo int auto_increment,
	nome varchar(30),
	idade int,
	primary key (codigo)
);

delimiter $$

create procedure inserir_nome (
	in novo_nome varchar(30),
	in nova_idade int
 )

begin

	insert into grupinho(nome, idade) values (novo_nome, nova_idade);
    
end

$$ delimiter ;

delimiter $$

create procedure alterar_dados (
in alt_codigo int,
in alt_nome varchar (30),
in alt_idade int)

begin
update grupinho set nome = alt_nome, idade = alt_idade where codigo = alt_codigo; 

end

$$ delimiter ;

delimiter $$

create procedure remover_dados (
in remover_nome varchar(20)
) 

begin
delete from grupinho where nome = remover_nome;

end

$$ delimiter ;

call inserir_nome("haylla", 21);

call alterar_dados(5 , "matheus", 23);

call remover_dados("gabriel");

select * from grupinho;

drop procedure alterar_dados;
drop procedure inserir_nome; 
drop procedure remover_dados;

drop database exercicios_procedure;