#h) Crie um vetor que peça cinco números, em seguida exiba os cinco números
#informados e mostre qual é o menor número e o maior número.


lista_de_numeros = []

menor_numero = 9999999999999999999999999

maior_numero = -9999999999999999999999999


for index in range(0, 5, 1):
    lista_de_numeros.append(int(input("Informe um numero: ")))

for index in range(0, len(lista_de_numeros), 1):
    print(lista_de_numeros[index])

for index in range(0, len(lista_de_numeros), 1):
    if lista_de_numeros[index] < menor_numero:
        menor_numero = lista_de_numeros[index]

    if lista_de_numeros[index] > maior_numero:
        maior_numero = lista_de_numeros[index]

print(f"o menor numero é {menor_numero}")

print(f"o maior numero é {maior_numero}")






