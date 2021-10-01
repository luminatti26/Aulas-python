#e) Faça com que sejam pedidos e armazenados cinco números. Informe quantos
#números dez foram informados pelo usuário


lista_de_numeros = []
contador = 0

for index in range(0, 5, 1):
    lista_de_numeros.append(int(input('Informe um numero: ')))

for index in range(0, 5, 1):
    if lista_de_numeros[index] == 10:
        contador += 1


print(f'O numero dez foi informado: {contador}')









