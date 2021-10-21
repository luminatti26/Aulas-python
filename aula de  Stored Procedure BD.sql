use relacionamento;

delimiter $$

create procedure inserir_cidade (
	in novo_nome varchar (15)
)
begin 
	insert into cidades(nome) values (novo_nome);
end

$$ delimiter ;

call inserir_cidade ("sorocaba");

select * from cidades;

drop procedure inserir_cidade;










