valor_1 = 12.00
valor_2 = 4.00
valor_3 = 16.00

pizza = valor_1
pao_de_queijo = valor_2
macarrao = valor_3


print("1 - Pizza $12.00")
print("2 - Pão de queijo $4.00")
print("3 - Macarrão $16.00")
print("******************************")

pedido = int(input("Informe o codigo do seu pedido: "))

if pedido == 1:
    valor_de_pagamento_1 = float(input("informe o valor de pagamento: "))
    if valor_de_pagamento_1 >= pizza:
        print(f'seu troco é de:{valor_de_pagamento_1 - pizza}')
        print("Bom apetite")
    else:
        print("valor informado não é suficiente")

elif pedido == 2:
    valor_de_pagamento_2 = float(input("informe o valor de pagamento: "))
    if valor_de_pagamento_2 >= pao_de_queijo:
        print(f'seu troco é de:{valor_de_pagamento_2 - pao_de_queijo}')
        print("Bom apetite")
    else:
        print("valor informado não é suficiente")

elif pedido == 3:
    valor_de_pagamento_3 = float(input("informe o valor de pagamento: "))
    if valor_de_pagamento_3 >= macarrao:
        print(f'seu troco é de:{valor_de_pagamento_3 - macarrao}' )
        print("Bom apetite")
    else:
        print("valor informado não é suficiente")

else:
    print("codigo não encontrado")

