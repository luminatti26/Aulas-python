#g) Haverá um cardápio contendo dez itens (você define o nome e o valor de cada item),
#cada item terá um código de 1 a 10, além do número 11 que finaliza o sistema.
#Enquanto não for digitado o número 11 será contabilizado em uma lista, quando
#digitado o número 11 exiba os produtos adquiridos e o total dessa compra.

caipirinha = 10
hot_dog = 24
cerveja = 8
agua = 4
refrigerante = 5
sorvete = 12
burrito = 16
taco = 20
hamburguer = 30
sanduiche = 28

soma_produtos = 0

valor = []
produto = []

print("selecione os itens que deseja no cardápio:\n"
          "1 - caipirinha = $10\n"
          "2 - hot dog = $24\n"
          "3 - cerveja = $8\n"
          "4 - agua = $4\n"
          "5 - refrigerante = $5\n"
          "6 - sorvete = $12\n"
          "7 - burrito = $16\n"
          "8 - taco = $20\n"
          "9 - hamburguer = $30\n"
          "10 - sanduiche = $28 \n"
          "\n"
          "11 - para fechar a conta\n")

while True:

    pedido = int(input(": "))

    if pedido == 1:
        valor.append(caipirinha)
        produto.append("caipirinha -")
    elif pedido == 2:
        valor.append(hot_dog)
        produto.append("hot dog -")

    elif pedido == 3:
        valor.append(cerveja)
        produto.append("cerveja -")

    elif pedido == 4:
        valor.append(agua)
        produto.append("agua -")

    elif pedido == 5:
        valor.append(refrigerante)
        produto.append("refrigerante -")

    elif pedido == 6:
        valor.append(sorvete)
        produto.append("sorvete -")

    elif pedido == 7:
        valor.append(burrito)
        produto.append("burrito -")

    elif pedido == 8:
        valor.append(taco)
        produto.append("taco -")

    elif pedido == 9:
        valor.append(hamburguer)
        produto.append("hamburguer -")

    elif pedido == 10:
        valor.append(sanduiche)
        produto.append("sanduiche -")

    elif pedido == 11:
        break

    else:
        print("codigo invalido")

for index in range(0,len(valor), 1):
    soma_produtos = soma_produtos + valor[index]

for index in range(0,len(produto), 1):
    print(produto[index],f'${valor[index]}')

print(f"total da sua conta: ${soma_produtos}")




