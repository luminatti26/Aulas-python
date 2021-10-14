from Fundamentos_python.classe_animal import Animal


class Aves(Animal):
    def __init__(self, cor_de_pena, velocidade_de_voo, largura_de_asa, quatidade_de_patas, tamanho, nome):
        super().__init__(quatidade_de_patas, tamanho, nome)
        self.cor_de_pena = cor_de_pena
        self.velocidade_de_voo = velocidade_de_voo
        self.largura_de_asa = largura_de_asa

    def locomover(self):
        print('Voar')


ave_1 = Aves("marrom", "10Km/h", "1M", 2, '50cm', "arara")

print(f'{ave_1.nome} tem {ave_1.tamanho} pussiu {ave_1.quatidade_de_patas} patas,'
      f' o tamanho de suas asas é de {ave_1.largura_de_asa}, a cor da pena é {ave_1.cor_de_pena} e '
      f'sua sua velocidade de voo é de {ave_1.velocidade_de_voo}')









