#f) Peça sete números, em seguida exiba a soma desses valores, a média e quantos
#números são maiores ou iguais a média.


lista_de_numeros = []
resultado_soma = 0
resultado_media = 0
resultado_iguais_ou_maiores_media = 0

for index in range(0, 7, 1):
    lista_de_numeros.append(int(input('Informe um numero: ')))

for index in range(0, len(lista_de_numeros), 1):
    resultado_soma = resultado_soma + lista_de_numeros[index]
print(resultado_soma)

for index in range(0, len(lista_de_numeros), 1):
    resultado_media = resultado_media + lista_de_numeros[index] / len(lista_de_numeros)
print(resultado_media)

for index in range(0, len(lista_de_numeros), 1):
    if lista_de_numeros[index] >= resultado_media:
        resultado_iguais_ou_maiores_media += 1
print( resultado_iguais_ou_maiores_media)
