#1) Crie um novo projeto chamado “ExerciciosLacosRepeticao”. Em sua classe Program.cs desenvolva um
#algoritmo que receba um número e escreva-o decrescendo de 1 em 1 até o valor chegar a zero.

#2) No mesmo projeto crie um novo método que receba do usuário números e enquanto não for passado um
#número PAR o programa solicite novamente. Passado o número par, calcule a metade desse número e chameo de X.
#Exiba na tela X vezes “Repetição” concatenado com o número atual das X vezes.

#3) No mesmo projeto, crie um novo procedimento em que pergunte ao usuário do sistema qual time ganhou a
#última copa do mundo de futebol. Dê a ele 4 opções, dentro dessas uma deve ser a verdadeira. Caso o usuário
#acerte, escreva “Acertou” caso contrário, “Errou”. Não pare o programa até que ele acerte a resposta


valor_1 = int(input('Digite um numero: '))

while valor_1 != -1:
    print(valor_1)
    valor_1 -= 1

def vir_par():
    contador = 0
    while True:
        valor_1 = int(input('informe um numero: '))
        resultado =  valor_1 % 2
        contador += 1
        if resultado == 0:
            x = valor_1 / 2
            break
    for index in range(1, contador, 1):
        print(f'{x:.0f} X {valor_1}')


vir_par()
