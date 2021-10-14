'''1) Crie um projeto e nomeie-o de “PythonPOO”. Seu projeto deverá:

a. Conter classes de animais. (Animais sugeridos, Pato, Gato, Cachorro)

b. Cada animal deve obrigatoriamente herdar de uma superclasse, sendo essa abstrata.

c. A superclasse deve conter o método abstrato EmitirSom ().

d. Cada um dos animais deve ser capaz de emitir som de seu próprio jeito.

e. O método principal deve ser capaz de visualizar as propriedades dos objetos, porém somente através do
método CadastrarAnimal () que as subclasses sobrescreverão (como sobrecarga) da classe pai, será possível
cadastra-los.

f. O método principal deve cadastrar cada um dos animais criados e atribui-los a um array da classe pai.

g. O método principal deve emitir o som de cada animal. '''

from Fundamentos_python.classes_para_exercicios import Pato, Gato, Cachorro


gato_1 = Gato('Boreal', 'Caramelo', 4)

pato_1 = Pato('Donald', 'Branca', 2)

cachorro_1 = Cachorro('Sirius', 'Preta', 4)

lista_de_animais = [gato_1, pato_1, cachorro_1]

print(f'O {gato_1.nome} é um gato da cor {gato_1.cor} e possui {gato_1.quantidade_de_patas} patas')

print(f'O {pato_1.nome} é um pato da cor {pato_1.cor} e possui {pato_1.quantidade_de_patas} patas')

print(f'O {cachorro_1.nome} é um cachorro da cor {cachorro_1.cor} e possui {cachorro_1.quantidade_de_patas} patas')

print('**********************************')

for index in range(0, 3, 1):
    lista_de_animais[index].emitir_som()





















