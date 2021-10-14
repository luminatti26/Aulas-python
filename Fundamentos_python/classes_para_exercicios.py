from abc import ABCMeta, abstractmethod


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

class Animal_2(metaclass=ABCMeta):
    def __init__(self, nome, quantidade_de_pata):
        self.nome = nome
        self.quantidade_de_pata = quantidade_de_pata

    @abstractmethod
    def locomover(self):
        raise Exception

class Ave_2(Animal_2, metaclass=ABCMeta):
    def __init__(self, cor_da_pena, nome, quantidade_de_pata):
        super().__init__(nome, quantidade_de_pata)
        self.cor_da_pena = cor_da_pena

class PatoRaivoso(Ave_2):
    def __init__(self, cor_da_pena, nome, quantidade_de_pata):
        super().__init__( cor_da_pena, nome, quantidade_de_pata)


    def locomover(self):
        print(f'{self.nome} esta voando com raiva!!')

class PatoSurfista(Ave_2):
    def __init__(self, cor_da_pena, nome, quantidade_de_pata):
        super().__init__( cor_da_pena, nome, quantidade_de_pata)

    def locomover(self):
        print(f'{self.nome} esta voando sobre as ondas!!')

class PythonPoo(metaclass=ABCMeta):
    def __init__(self, nome, cor, quantidade_de_patas):
        self.nome = nome
        self.cor = cor
        self.quantidade_de_patas = quantidade_de_patas

    @abstractmethod
    def emitir_som(self):
        raise Exception

class Pato(PythonPoo):
    def __init__(self, nome, cor, quantidade_de_patas):
        super(). __init__(nome, cor, quantidade_de_patas)

    def emitir_som(self):
        print(f'O {self.nome} fez quack!! quack!!')

class Gato(PythonPoo):
    def __init__(self, nome, cor, quantidade_de_patas):
        super().__init__(nome, cor, quantidade_de_patas)

    def emitir_som(self):
        print(f'O {self.nome} fez miu!!')

class Cachorro(PythonPoo):
    def __init__(self, nome, cor, quantidade_de_patas):
        super().__init__(nome, cor, quantidade_de_patas)

    def emitir_som(self):
        print(f'O {self.nome} fez au! au!')

