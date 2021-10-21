import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database='exercicio_cadastro_DB',
    user='root',
    password='lucas26'
)

def cadastro(nome, email, cargo, idade):
    try:
        cursor = db.cursor()
        sql = 'INSERT INTO perfil (nome, email, cargo, idade) VALUES (%s, %s, %S, %S)'
        info = (nome, email, cargo, idade)
        cursor.execute(sql, info)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)

def alter():
    try:
        cursor = db.cursor()
        sql = 'select * from pessoa'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for index in range(0, len(resultado), 1):
            print(resultado(index))
            opcao = int(input('informe o número do contato que deseja alterar: '))
            sql = 'update pessoa set nome = %s where primary key = %s'

            cursor.execute(sql, parametros)

        cursor.close()
    except Exception as error:
        print(error)

def delete():
    try:
        cursor = db.cursor()
        sql = 'select * from pessoa'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for index in range(0, len(resultado), 1):
            print(resultado(index))
            codigo = int(input('informe o número do contato que deseja deletar: '))
            sql = f'delete from pessoa where primary key = "{codigo}"'
            cursor.execute(sql)
            db.commit()
        cursor.close()
    except Exception as error:
        print(error)

