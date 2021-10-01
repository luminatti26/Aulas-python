#O usuário informa um número inicial e um número final, em seguida retorne a
#quantidade de pares e ímpares daquela cadeia de valores.
#Vamos supor que os números informados foram: 6 e 12, sendo assim serão 4
#pares (6, 8, 10 e 12) e 3 ímpares (7, 9 e 11).

valor_1 = float(input('Digite o numero inicial: '))
valor_2 = float(input('Digite o numero final: '))

for index in range(valor_1, valor_2,1):
resultado_modulo = valor_1 % 2
if resultado_modulo == 0
    print('o valor', resultado_modulo, 'é par')
else:
    print('o valor', resultado_modulo, 'é impar')



