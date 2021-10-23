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
from MySQL.def_exercicios import cadastro,alter, delete, vizualizar

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
          '4 - Visualizar lista\n'
          '5 - Sair')
    opcao = int(input(': '))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        alter()

    elif opcao == 3:
        delete()
    elif opcao == 4:
        vizualizar()
    elif opcao == 5:
        break
    else:
        input('Opção inválida.')

print('Muito obrigado...')








