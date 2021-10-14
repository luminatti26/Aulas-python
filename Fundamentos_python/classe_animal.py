from abc import ABCMeta, abstractmethod



class Animal(metaclass=ABCMeta):
    def __init__(self, quatidade_de_patas, tamanho, nome):
        self.quatidade_de_patas =quatidade_de_patas
        self.tamanho = tamanho
        self.nome = nome

    @abstractmethod
    def locomover(self):
        raise Exception()
















