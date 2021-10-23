import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database='contatos',
    user='root',
    password='lucas26'
)


class BancoDeDados():
    def __init__(self):
        pass


    def cadastrar(self):
        print('Para cadastrar um novo contato...')
        novo_contato = (input('Informe nome do contato: '),
                        input('Informe o sobrenome do contato: '),
                        input('Informe o CPF do contato: '),
                        input('Informe o email do contato: '),
                        input('Informe o telefone do contato'))
        try:
            cursor = db.cursor()
            sql = 'INSERT INTO perfil (nome, sobrenome, cpf, email, telefone) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(sql, novo_contato)
            db.commit()
            cursor.close()
        except Exception as error:
            print(error)



    def alterrar(self):
        pass


    def deletar(self):
        pass


    def visualizar(self):
        pass