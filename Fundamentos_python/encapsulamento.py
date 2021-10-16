'''Criar um novo projeto chamado supermercado.Neste projeto existirá:

1. Classe chamada Caixa

- O Caixa deve possuir as seguintes caracteristicas: numero_caixa, valor_em_caixa
- Somente será permitido que um atendente de caixa consiga adicionar ou retirar dinheiro deste caixa.

2. Classe chamada Pessoa

- A classe Pessoa deve ser abstrata.
- Deve possuir as seguintes características: nome, cpf

3. Classe chamada Atendente de Caixa

- A classe deve herdar da classe Pessoa
- Deve possuir a ação de incluir e retirar dinheiro do caixa.

4. Classe chamada Cliente

- A classe deve herdar da classe Pessoa
- Deve possuir a caracteristica de valor_em_carteira'''

from Fundamentos_python.classes_para_exercicios import AtendenteDeCaixa, Caixa, Cliente

if __name__ == '__main__':

    lucao = Cliente('Lucão', '11575296900', 100.00)

    caixa_1 = Caixa(1, 200.00)

    atendente_1 = AtendenteDeCaixa('João', '12345678900', caixa_1)

    atendente_1.inserir_no_caixa(50.00)

    atendente_1.retirar_do_caixa(25.00)

    print(caixa_1._valor_em_caixa)















