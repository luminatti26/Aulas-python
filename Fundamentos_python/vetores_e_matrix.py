"""2 – Crie um vetor com 10 posições do tipo inteiro, preencha seus valores “hard coded”. Para este vetor crie
dinamicamente uma lista do tipo inteiro que receba a multiplicação de cada valor do vetor por dez. Ao final
exiba todos os valores de ambos na tela.

3 – Crie uma matriz que receba o nome de 5 pessoas. Posterior ao preenchimento dos primeiros nomes,
receba o segundo nome dessas mesmas pessoas, dizendo “Qual é sobrenome do”, concatenado o primeiro
nome. No final exiba todos os nomes e sobrenomes na tela."""


"""lista_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_2 = []

for index in range(0, len(lista_1), 1):
    valor_1 = lista_1[index] * 10
    lista_2.append(valor_1)

for i in lista_1:
    print(i)

for ind in lista_2:
    print(ind)"""



nomes_sobrenomes = [ [], [] ]

for index in range(0, 5, 1):
    nomes_sobrenomes[0].insert(index, input('Informe o nome do usuario: '))

for index in range(0, 5, 1):
    nomes_sobrenomes[1].insert(
                    index,
                    input(f'Informe o sobre sobrenome do usuario'
                          f' {nomes_sobrenomes[0][index]}: '))

for index in range(0, 1, 1):
    for index_2 in range(0, 5, 1):
        print( f'{nomes_sobrenomes[index][index_2]} {nomes_sobrenomes[index + 1][index_2]}')
