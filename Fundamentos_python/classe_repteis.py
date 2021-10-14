from Fundamentos_python.classe_animal import Animal


class Repteis(Animal):
    def __init__(self, cor_de_escama, velocidade_de_rastejo, largura_de_calda, quatidade_de_patas, tamanho, nome):
        super().__init__(quatidade_de_patas, tamanho, nome)
        self.cor_de_escama = cor_de_escama
        self.velocidade_de_rastejo = velocidade_de_rastejo
        self.largura_de_calda = largura_de_calda

    def locomover(self):
        print('rasteja')


reptil_1 = Repteis('cinza', '5Km/h', '30cm', 4, '1m', 'largatixa')

print(f'o reptil {reptil_1.nome} pussui escamas na cor {reptil_1.cor_de_escama}, '
      f'possui um comprimento de {reptil_1.tamanho}, o tamanho da sua calda é {reptil_1.largura_de_calda}, '
      f'pussui {reptil_1.quatidade_de_patas} e sua velocidade é de {reptil_1.velocidade_de_rastejo}')

















