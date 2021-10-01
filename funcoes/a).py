#a) Crie um formulário, onde o usuário irá informar dois valores e uma operação
#de soma, subtração, multiplicação ou divisão.
#Haverá as seguintes funções:
#1) Ação - Responsável por obter os dados informados, selecionar um cálculo e exibir
#2) Soma - Haverá dois parâmetros que retornará a soma dos valores
#3) Subtração - Haverá dois parâmetros que retornará a subtração dos valores
#4) Multiplicação - Haverá dois parâmetros que retornará a multiplicação dos valores
#5) Divisão - Haverá dois parâmetros que retornará a divisão dos valores


def soma(valor_1, valor_2):
    resultado = valor_1 + valor_2
    return resultado

def subtracao(valor_1, valor_2):
    resultado = valor_1 - valor_2
    return resultado

def multiplicacao(valor_1, valor_2):
    resultado =  valor_1 * valor_2
    return resultado

def divisao(valor_1, valor_2):
    resultado = valor_1 /valor_2
    return resultado

print('Insira os valores abaixo')
informacao_1 = int(input(': '))
informacao_2 = int(input(': '))

print('Informe a operação que deseja fazer:\n',
      '1 - soma\n',
      '2 - subtração\n',
      '3 - multiplicação\n',
      '4 - divisão')

opcao = int(input(': '))
if opcao == 1:
    resultado_soma = soma(informacao_1, informacao_2)

    print(resultado_soma)

elif opcao == 2:
    resultado_subtracao = subtracao(informacao_1, informacao_2)

    print(resultado_subtracao)

elif opcao == 3:
    resultado_multiplicacao = multiplicacao(informacao_1, informacao_2)

    print(resultado_multiplicacao)

elif opcao == 4:
    resultado_divisao = divisao(informacao_1, informacao_2)

    print(resultado_divisao)

else:
    print('Operação inválida')




