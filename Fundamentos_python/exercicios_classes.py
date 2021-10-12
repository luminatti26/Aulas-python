'''Crie uma classe Animal
Carateristicas obrigatórias: nome, quantidade_de_patas, cor, tipo_de_pelo
Caracteristicas opcionais: idade tamanho
Ações: andar, rugir
Se o animal andou duas vezes ele esta cansado e não consegue rugir
Obrigatório receber dados via input
Criar a classe em um arquivo e criar o objeto em outro'''

from Fundamentos_python.classes_para_exercicios import Animal




animal_1 = Animal(input('Qual o nome do Animal?: '),
                  input(f'Quantas patas tem?: '),
                  input('Qual a cor?: '),
                  input('Qual o tipo de pelo?: '))


print(f'Gostaria de informar a idade do(a) {animal_1.nome}:')
resposta_1 = input('[s] p/ sim ou [n] p/ não: ')
if resposta_1 == 's':
    animal_1.idade = int(input('Quantos anos ele(a) tem: '))

print(f'Gostaria de informar o tamanho do(a) {animal_1.nome}:')
resposta_2 = input('[s] p/ sim ou [n] p/ não: ')
if resposta_2 == 's':
    animal_1.tamanho = int(input('Qual o tamanho dele(a) em cm: '))

while True:
    print(f'O que quer fazer {animal_1.nome}\n'
          f'1 - andar\n'
          f'2 - rugir\n'
          f'3 - deixa-lo em paz')
    resultado = input(': ')
    if resultado == '1':
        animal_1.andar()
    elif resultado == '2':
        animal_1.rugir()
    elif resultado == '3':
        break

    else:
        print('Vou perguntar novamente.')
