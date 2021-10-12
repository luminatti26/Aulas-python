'''class Pessoa ():
    def __init__(self, nome, sobrenome, idade):
        self.nome = ''
        self.sobrenome = ''
        self.idade = 0

pessoa_1 = Pessoa()'''


# crie uma classe caneta:
# Caracteristicas da caneta - comprimento, cor, tipo_ponta
# Duas ações - abrir e fechar (pode ser um print dizendo abrindo a caneta e outro dizendo fechando a caneta)
# Caracteristicas são atributos (lembrem das variaveis)
# açoes são funções/metodos (lembrem das funções)
# Crie 3 objetos a partir da classe caneta e exiba suas caracteristicas e ações na tela (print)

class Caneta():
    def __init__(self, comprimento, cor, tipo_ponta, nome, marca):
        self.comprimento = comprimento
        self.cor = cor
        self.tipo_ponta = tipo_ponta
        self.nome = nome
        self.marca = marca

    def abrir(self):
        print(f'Você abriu a caneta {self.nome}.')

    def fechar(self):
        print(f'Você fechou a caneta {self.nome}.')


caneta_1 = Caneta('10.5cm', 'Azul', 'Esferográfica', 'BIC Cristal', 'BIC')

caneta_2 = Caneta('10cm', 'Amarelo', 'Marca Texto', 'SM1557','Faber Castell')

caneta_3 = Caneta('10,3cm', 'Preta', 'Caneta Nankin', 'PIGMA MICRON 04', 'SAKURA')

print(f'Eu tenho 3 canetas, elas são {caneta_1.nome} {caneta_1.cor}, {caneta_2.nome} {caneta_2.cor} e \n'
      f'{caneta_3.nome} {caneta_3.cor}, suas marcas são respectivamente {caneta_1.marca},\n'
      f'{caneta_2.marca} e {caneta_3.marca}.\n'
      f'A caneta {caneta_1.nome} é {caneta_1.tipo_ponta} e tem {caneta_1.comprimento},\n'
      f'a caneta {caneta_2.nome} é {caneta_2.tipo_ponta} e tem {caneta_2.comprimento} e \n'
      f'a caneta {caneta_3.nome} é {caneta_3.tipo_ponta} e tem {caneta_3.comprimento}.')

caneta_1.abrir()
caneta_1.fechar()
caneta_2.abrir()
caneta_2.fechar()
caneta_3.abrir()
caneta_3.fechar()











