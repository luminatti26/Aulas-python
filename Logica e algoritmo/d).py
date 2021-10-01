print("informe três numeros")
print("**************************")
valor_1 = float(input("primeiro numero: "))
valor_2 = float(input("segundo numero: "))
valor_3 = float(input("terceiro numero:"))

if valor_1 < valor_2 and valor_1 < valor_3:
    print(valor_1)
elif valor_2 < valor_1 and valor_2 < valor_3:
    print(valor_2)
elif valor_3 < valor_1 and valor_3 < valor_2:
    print(valor_3)
else:
    print(valor_1)