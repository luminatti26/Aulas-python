''' 1 - Crie um projeto chamado cadastro e dentro desse projeto faça uma lógica para:
a. Salvar um novo usuário passando nome, e-mail, cargo e idade
b. Quando quiser alterar um usuário já cadastrado, tem de ter uma opção para que eu possa ver todos os
usuários já cadastrados e possa escolher o número de um para alterar
c. Tem de ter uma opção para excluir usuários, também antes mostrando todos os usuários já
cadastrados e escolhendo um número para ser removido
Obs: Quando iniciar a aplicação temos de perguntar a o usuário qual operação ele deseja realizar, sempre
seguindo os tópicos acima.
Para esse exercício utilizaremos o banco de dados e a orientação a objetos.
2 – No mesmo Exercício crie um filtro de dados para poder pesquisar um usuário pelo nome '''
import mysql.connector
from MySQL.def_exercicios import cadastro,alter, delete

db = mysql.connector.connect(
    host='localhost',
    database='exercicio_cadastro_DB',
    user='root',
    password='lucas26'
)

try:
    cursor = db.cursor()
    print('conectou no banco')
    cursor.close()
except Exception as error:
    print(error)

while True:
    print('Informe a operação que deseja fazer:\n'
          '1 - Cadastrar novo contato.\n'
          '2 - Alterar contato.\n'
          '3 - Excluir contato.\n'
          '4 - Sair')
    opcao = int(input(': '))
    if opcao == 1:
        nome = input('Informe o nome do contato: ')
        email = input('Informe o e-mail do contato: ')
        cargo = input('Informe o cargo do contato: ')
        idade = int(input('Informe a idade do contato: '))
        cadastro(nome, email, cargo, idade)
    elif opcao == 2:
        alter()
        pass

    elif opcao == 3:
        delete()
        pass

    elif opcao == 4:
        break
    else:
        input('Opção inválida.')

print('Muito obrigado...')








