class Animal():
    def __init__(self, nome, quantidade_de_patas, cor, tipo_de_pelo):
        self.nome = nome
        self.quantidade_de_patas = quantidade_de_patas
        self.cor = cor
        self.tipo_de_pelo = tipo_de_pelo
        self.idade = 0
        self.tamanho = 0
        self.contador_andar = 0

    def andar(self):
        print(f'O {self.nome} andou.')
        self.contador_andar += 1



    def rugir(self):
        if self.contador_andar >= 2:
            print(f'O {self.nome} andou demais e esta cansado para rugir.\n'
                  f'Descanse para Rugir.')
            self.contador_andar -= 1

        else:
            print(f'O {self.nome} rugiu.')
            if self.contador_andar > 0:
                self.contador_andar -= 1


















