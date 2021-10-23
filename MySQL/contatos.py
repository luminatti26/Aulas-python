'''Python e Mysql
Criar um CRUD simples usando funções ou orientação objeto
Cada operação deve estar isolada (uma função para cada operação)(pode ser orientado a obejeto)
Validar os campos e não ter informações duplicadas (validar pelo cpf)
cadastro de contatos.
ID (primary key auto_increment), nome, sobrenome, CPF (unique), email, telefone'''
import mysql.connector
from MySQL.class_def_exercicio_contatos import BancoDeDados
db = mysql.connector.connect(
    host='localhost',
    database='contatos',
    user='root',
    password='lucas26'
)

try:
    cursor = db.cursor()
    print('conectou no banco')
    cursor.close()
except Exception as error:
    print(error)

BancoDeDados.cadastrar()
