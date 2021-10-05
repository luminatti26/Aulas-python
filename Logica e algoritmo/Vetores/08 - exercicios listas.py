# a) Crie um vetor contendo cinco cidades, em seguida exiba seus valores.

lista_de_cidades = ['Blumenau', 'Pomerode', 'Gaspar', 'Balneário Camboriú', 'Joinville']

for index in range(0, len(lista_de_cidades), 1):
    print(lista_de_cidades[index])

# b) Desenvolva um sistema que o usuário informa cinco números através do comando
# prompt, em seguida exiba os valores informados e mostre a soma desses valores.

lista_de_valores = []
soma_dos_valores = 0

for index in range(0, 5, 1):
    lista_de_valores.append(int(input('Informe um número: ')))

print('Os valores informados são: ', end=' ')
for index in range(0, len(lista_de_valores), 1):
    print(lista_de_valores[index], end=' ')
    soma_dos_valores = soma_dos_valores + lista_de_valores[index]
print('')

print(f'E a soma dos valores é: {soma_dos_valores}')
print(f'E a soma dos valores é: {sum(lista_de_valores)}')

# c) Crie um laço que peça nomes, poderão ser armazenados vários nomes, não há uma
# quantidade mínima nem máxima. Quando informada a palavra sair, exiba todos os
# nomes e informe a quantidade de nomes cadastrados.

lista_de_nomes = []

while True:
    lista_de_nomes.append(input('Informe um nome: '))

    if 'sair' == input('Digite "sair" para encerrar o programa ou enter para continuar:  ').lower():
        break

print(f'Os nomes informados são: ', end='')
for index in range(0, len(lista_de_nomes), 1):
    if index != len(lista_de_nomes) - 1:
        print(lista_de_nomes[index], end=', ')
    else:
        print(lista_de_nomes[index], end='.')
print('')
print(f'A quantidade de nomes informados é: {len(lista_de_nomes)}')


# d) O usuário informa cinco números, em seguida exiba na ordem contrário que foram
# informados.

lista_de_numeros = []

for index in range(0, 5, 1):
    lista_de_numeros.append(int(input('Informe um número: ')))
print(f'Os números em ordem contrária são: ', end=' ')
for index in range(len(lista_de_numeros) - 1, -1, -1):
    print(lista_de_numeros[index], end=' ')

# e) Faça com que sejam pedidos e armazenados cinco números. Informe quantos
# números dez foram informados pelo usuário.

lista_de_numeros = []

for index in range(0, 5, 1):
    lista_de_numeros.append(int(input('Informe um número: ')))

contador = 0

for index in range(0, 5, 1):
    if lista_de_numeros[index] == 10:
        contador += 1

print(f'A quantidade de números dez informados pelo usuário são: {contador} vezes.')


# f) Peça sete números, em seguida exiba a soma desses valores, a média e quantos
# números são maiores ou iguais a média

lista_de_numeros = []

for index in range(0, 7, 1):
    lista_de_numeros.append(int(input('Informe um número: ')))

soma = 0
media = 0
count = 0

for index in range(0, 7, 1):
    soma += lista_de_numeros[index]

media = soma / 7

for index in range(0, 7, 1):
    if lista_de_numeros[index] >= media:
        count += 1

print(f'A soma dos números informados é de: {soma}', end='\n')
print(f'A média dos números informados é de: {media}', end='\n')
print(f'A quantidade de números que são iguais ou maiores que a média é de: {count}')

# g) Haverá um cardápio contendo dez itens (você define o nome e o valor de cada item),
# cada item terá um código de 1 a 10, além do número 11 que finaliza o sistema.
# Enquanto não for digitado o número 11 será contabilizado em uma lista, quando
# digitado o número 11 exiba os produtos adquiridos e o total dessa compra.

cardapio = ['Informe o código do produto que deseja adquirir: ', '[1] - Pastel de frango - R$ 2.50',
            '[2] - Pastel de carne - R$ 2.50', '[3] - Cachorro quente - R$ 4.00',
            '[4] - Coxinha - R$ 3.50', '[5] - Misto quente - R$ 3.00', '[6] - Suco de Uva - R$ 4.00',
            '[7] - Vitamina de morango - R$ 5.00', '[8] - Refrigerante - R$ 5.00',
            '[9] - Torta de Limão - R$ 6.00', '[10] - Sorvete - R$ 7.00', '[11] - Finalizar a compra.']

produtos = ['', 'Pastel de frango', 'Pastel de carne', 'Cachorro quente', 'Coxinha', 'Misto quente', 'Suco de Uva',
            'Vitamina de morango', 'Refrigerante', 'Torta de Limão', 'Sorvete']

valores = [0, 2.50, 2.50, 4.00, 3.50, 3.00, 4.00, 5.00, 5.00, 6.00, 7.00]

pedido_final = []

total_da_compra = 0

while True:
    for index in range(0, 12, 1):
        print(cardapio[index], end='\n')
    codigo = int(input())
    if codigo == 11:
        break
    pedido_final.append(produtos[codigo])
    total_da_compra += valores[codigo]

print('Os produtos adquiridos foram: ')
for index in range(0, len(pedido_final), 1):
    print(pedido_final[index])
print(f'O valor total da compra foi de: {total_da_compra}')

# h) Crie um vetor que peça cinco números, em seguida exiba os cinco números
# informados e mostre qual é o menor número e o maior número.

lista_de_numeros = []

for index in range(0, 5, 1):
    lista_de_numeros.append(int(input('Informe um número: ')))

print('Os números informados são: ')
for index in range(0, 5, 1):
    print(lista_de_numeros[index])

menor = 9999999999999999
maior = -9999999999999999
for index in range(0, 5, 1):
    if lista_de_numeros[index] < menor:
        menor = lista_de_numeros[index]
    if lista_de_numeros[index] > maior:
        maior = lista_de_numeros[index]

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')


# i) Desenvolva um sistema para gerenciar cursos, as funcionalidades pedidas são:
# 1) Cadastrar curso - Pede o nome do novo curso
# 2) Selecionar cursos - Exibe todos os cursos
# 3) Remover curso - Pede o nome do curso e realiza a exclusão
# 4) Sair do sistema - Finaliza o laço

cursos = []

while True:
    codigo = int(input('Informe [1] - Para cadastrar um novo curso\n'
                       'Informe [2] - Para exibir todos os cursos\n'
                       'Informe [3] - Para remover um curso\n'
                       'Informe [4] - Para sair do sistema\n'
                       ''))

    if codigo == 1:
        cursos.append(input('Informe o nome do novo curso: '))
    if codigo == 2:
        print('Os cursos existentes são: ')
        for index in range(0, len(cursos), 1):
            print(cursos[index])
    if codigo == 3:
        cursos.remove(input('Informe o curso que deseja remover: '))
    if codigo == 4:
        break
