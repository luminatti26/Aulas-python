print('informe o tamanho de cada lado de um triangulo')

valor_1 = float(input('informe o tamanho do lado direito: '))
valor_2 = float(input('informe o tamanho do lado inferior: '))
valor_3 = float(input('informe o tamanho do lado esquerdo: '))

direito = valor_1
inferior = valor_2
esquerdo = valor_3
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')
if direito == inferior and inferior == esquerdo:
    print('seu triangulo é equilatero')
elif direito == inferior and inferior != esquerdo:
    print('seu triangulo é isosceles')
elif direito != inferior and inferior == esquerdo:
    print('seu triangulo é isosceles')
elif direito !=inferior and direito == esquerdo:
    print('seu triangulo é isosceles')
else:
    print('seu triangulo é escaleno')







