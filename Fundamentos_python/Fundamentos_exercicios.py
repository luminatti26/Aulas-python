# 1- Crie uma aplicação que calcule o IMC do indivíduo, pesquise a fórmula e aplique

def imc(peso_1, altura_1):

    resultado_imc = peso_1 / pow(altura, 2)

    return resultado_imc


print('Para calcular seu IMC informe abaixo:')

peso = float(input('Seu peso em Kg: '))
altura = float(input('Sua altura em Metros: '))

resultado = imc(peso, altura)

print('***********************************************')

if resultado >= 18.5 and resultado <= 24.9:
    print(f'{resultado:.1f} Seu IMC esta normal')

elif resultado < 18.5:
    print(f'{resultado:.1f} Seu IMC esta abaixo do normal')

elif resultado > 24.9:
    print(f'{resultado:.1f} Seu IMC esta acima do normal')
