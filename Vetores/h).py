#h) Crie um vetor que peça cinco números, em seguida exiba os cinco números
#informados e mostre qual é o menor número e o maior número.


lista_de_numeros = []

menor_numero = 0

maior_numero = 0

for index in range(0, 5, 1):
    lista_de_numeros.append(int(input("Informe um numero: ")))

for index in range(0, len(lista_de_numeros), 1):
    print(lista_de_numeros[index])










