primeira_nota = float(input("informe a primeira nota: "))
print('***************************')
segunda_nota = float(input("informe a segunda nota: "))
print('***************************')

soma_da_nota = (primeira_nota + segunda_nota)
media = (soma_da_nota / 2)

if  media >= 7:
    print(media)
    print("aprovado")

    print(media)
else:
    print("reprovado")