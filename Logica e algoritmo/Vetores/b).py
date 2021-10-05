#b) Desenvolva um sistema que o usuário informa cinco números através do comando
#prompt, em seguida exiba os valores informados e mostre a soma desses valores.



lista_de_numeros = []

resultado_soma = 0

for index in range(0, 5, 1):
    lista_de_numeros.append(int(input('Informe um novo numero: ')))

for index in range(0, len(lista_de_numeros), 1):
    print(lista_de_numeros[index])

for index in range(0, len(lista_de_numeros), 1):
    resultado_soma = resultado_soma + lista_de_numeros[index]
print(resultado_soma)
