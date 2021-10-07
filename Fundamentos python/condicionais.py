#1) Em seu projeto python desenvolva um algoritmo que receba a idade do usuário e:
#a. Se a idade for maior ou igual a 13 e menor que 19 escreva “Adolescente”.
#b. Se a idade for maior ou igual a 19 e menor ou igual a 60 escreva “Adulto”.
#c. Se a idade for maior que 60 escreva “Idoso”.
#d. Caso contrário escreva “Criança”.
#2) No mesmo projeto, crie um novo procedimento em que pergunte ao usuário do sistema qual time ganhou a
#copa do mundo de futebol de 2014. Dê a ele 4 opções, dentro dessas uma deve ser a verdadeira. Caso o
#usuário acerte, escreva “Acertou” caso contrário “Errou”.
#3) Utilize o mesmo projeto de IMC dos módulos anteriores e exiba o a classificação de acordo com o resultado
#(ex: abaixo do peso, sobrepeso, obesidade, etc).


idade = int(input('informe a sua idade: '))

if idade >= 13 and idade < 19:
    print('Adolescente')

elif idade >= 19 and  idade <= 60:
    print('Adulto')

elif idade > 60:
    print('Idoso')

else:
    print('Criança')

print('**************************************')

print('Qual seleção ganhou a copa do mundo de 2014:\n'
      '1 - Brasil\n'
      '2 - Argentina\n'
      '3 - Alemanha\n'
      '4 - Holanda')

resultado = int(input(': '))

if resultado == 3:
    print('Acertou!\n'
          'Mais um da Alemanha!! VIROU PASSEIO!!')

else:
    print('Errou!')















