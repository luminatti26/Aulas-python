'''Criar uma classe Animal que será abstrata(não pode ser criado objetos com ela)
Essa classe possui caracteristicas nome, quantidade de patas,
Essa classe possui a ação de locomover

Criar uma classe Ave que será abstrata e possui caracteristica de cor de pena
a classe Ave herda da classe Animal

Criar uma classe PatoRaivoso que não será abstrata e possui comportamento de voar com raiva

Criar uma classe PatoSurfista que não será abstrata e possui comportamento de voar sobre as ondas

As classes de patos herdam da classe Ave

No final, exiba cada caracteristica dos objetos criados(um de PatoRaivoso e outro de PatoSurfista )
Exiba o comportamento de se locomover'''

from Fundamentos_python.classes_para_exercicios import PatoSurfista, PatoRaivoso

pato_bravo = PatoRaivoso('Preta', 'Eduardo', 2)

pato_legal = PatoSurfista('Brancas', 'Matheus', 2)


print(f'O pato {pato_bravo.nome} tem a cor das penas {pato_bravo.cor_da_pena} '
      f'e possui {pato_bravo.quantidade_de_pata} patas')

pato_bravo.locomover()

print(f'O pato {pato_legal.nome} tem a cor das penas {pato_legal.cor_da_pena} '
      f'e possui {pato_legal.quantidade_de_pata} patas')

pato_legal.locomover()














