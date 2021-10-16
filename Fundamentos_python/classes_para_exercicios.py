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

class Caixa():
    def __init__(self, numero_caixa, valor_em_caixa):
        self.numero_caixa = numero_caixa
        self._valor_em_caixa = valor_em_caixa

    def set_validacao(self, usuario):
        if isinstance(usuario, AtendenteDeCaixa):
            pass
        else:
            print('Você não é um atendende')

class Pessoa(metaclass=ABCMeta):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class AtendenteDeCaixa(Pessoa):
    def __init__(self, nome, cpf, caixa_relacionado):
        super().__init__(nome, cpf)
        self.caixa_relacionado = caixa_relacionado


    def inserir_no_caixa(self, valor_1):
        self.caixa_relacionado._valor_em_caixa += valor_1
        print(f'{self.nome} inseriu R${valor_1} no caixa')

    def retirar_do_caixa(self, valor_1):
        self.caixa_relacionado._valor_em_caixa -= valor_1
        print(f'{self.nome} retirou R${valor_1} no caixa')

class Cliente(Pessoa):
    def __init__(self, nome, cpf, valor_em_carteira):
        super().__init__(nome, cpf)
        self.valor_em_carteira = valor_em_carteira
        self.caixa_furtado = 0

    def pagamento(self, valor_1):
        pass












