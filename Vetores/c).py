#c) Crie um laço que peça nomes, poderão ser armazenados vários nomes, não há uma
#quantidade mínima nem máxima. Quando informada a palavra sair, exiba todos os
#nomes e informe a quantidade de nomes cadastrados.

nomes_cadastrados = []

finalizar = 'N'

while finalizar != 'S':
    nomes_cadastrados.append(input('Informe um nome para cadastro: '))

    finalizar = input('Deseja sair do cadastro? [S] ou [N]: ')


for index in range(0, len(nomes_cadastrados), 1):
    print(nomes_cadastrados[index])
print(len(nomes_cadastrados))




