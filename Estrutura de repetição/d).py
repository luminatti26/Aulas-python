#Crie uma estrutura de laços de repetição que exiba a seguinte estrutura:
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1


for index in range(5, 0, -1):
    for index_2 in range(index, 0, -1):
        print(index_2, end=" ")
    print("")










