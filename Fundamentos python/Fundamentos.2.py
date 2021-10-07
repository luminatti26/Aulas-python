#1 – Crie um programa com as seguintes funções:
#a. Receba três parâmetros, um Nome (nome e sobrenome), uma idade e um telefone (somente números).
#b. Faça uma rotina para padronizar o formato do telefone (xx)99999-9999 na tela.
#c. Faça uma rotina que calcule a raiz quadrada da idade do usuário e retorne para o método principal um
#double, que será exibido na tela.
#d. Faça uma rotina para que troque os espaços entre os nomes do usuários por “;” e exiba na tela

import math

def raiz(idade):
    raiz_idade = math.sqrt(idade)

    return raiz_idade

def nome_sobrenome(nome):
    novo_nome = nome.replace(' ', '; ')

    return novo_nome


def padronizar(telefone):
    forma_padrao = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:11]}'

    return forma_padrao





print('informe os seguintes dados. ')

nome = input('informe nome e sobre-nome: ')

idade = int(input('informe a idade: '))

telefone = input('informe o telefone:')





print(nome_sobrenome(nome))
print(raiz(idade))
print(padronizar(telefone))



















