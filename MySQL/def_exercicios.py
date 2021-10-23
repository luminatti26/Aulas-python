import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database='exercicio_cadastro_DB',
    user='root',
    password='lucas26'
)


def cadastro():
    nome = input('Informe o nome do contato: ')
    email = input('Informe o e-mail do contato: ')
    cargo = input('Informe o cargo do contato: ')
    idade = int(input('Informe a idade do contato: '))
    try:
        cursor = db.cursor()
        sql = 'INSERT INTO perfil (nome, email, cargo, idade) VALUES (%s, %s, %s, %s)'
        info = (nome, email, cargo, idade)
        cursor.execute(sql, info)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)


def alter():
    vizualizar()
    codigo = int(input('Selecione o numero do contato que deseja editar: '))
    if codigo > 0:
        print('O que deseja alterar?: \n'
              '1 - Nome\n'
              '2 - Email\n'
              '3 - Cargo\n'
              '4 - Idade\n'
              '5 - Sair')
        opcao_1 = int(input(': '))
        if opcao_1 == 1:
            novo_nome = input('Informe o novo nome do contato: ')
            try:
                parametros = (novo_nome, codigo)
                cursor = db.cursor()
                sql = 'update perfil set nome = %s where codigo = %s'
                cursor.execute(sql, parametros)
                db.commit()
                cursor.close()
            except Exception as error:
                print(error)

        elif opcao_1 == 2:
            novo_email = input('Informe o novo email do contato: ')
            try:
                parametros = (novo_email, codigo)
                cursor = db.cursor()
                sql = 'update perfil set email = %s where codigo = %s'
                cursor.execute(sql, parametros)
                db.commit()
                cursor.close()
            except Exception as error:
                print(error)

        elif opcao_1 == 3:
            novo_cargo = input('Informe o novo cargo do contato: ')
            try:
                parametros = (novo_cargo, codigo)
                cursor = db.cursor()
                sql = 'update perfil set cargo = %s where codigo = %s'
                cursor.execute(sql, parametros)
                db.commit()
                cursor.close()
            except Exception as error:
                print(error)

        elif opcao_1 == 4:
            nova_idade = input('Informe a nova idade do contato: ')
            try:
                parametros = (nova_idade, codigo)
                cursor = db.cursor()
                sql = 'update perfil set idade = %s where codigo = %s'
                cursor.execute(sql, parametros)
                db.commit()
                cursor.close()
            except Exception as error:
                print(error)

        else:
            print('Numero invalido.')

    else:
        print('Numero invalido')


def delete():
    vizualizar()
    codigo = int(input('Selecione o numero do contato que deseja apagar: '))
    if codigo > 0:
        try:
            cursor = db.cursor()
            sql = f'delete from perfil where codigo = "{codigo}"'
            cursor.execute(sql)
            db.commit()
            cursor.close()
        except Exception as error:
            print(error)
    else:
        print('Numero invalido')


def vizualizar():
    try:
        cursor = db.cursor()
        sql = 'select * from perfil'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for index in resultado:
            print(f'#{index[0]} | {index[1]} | {index[2]} | {index[3]} | {index[4]}')
        cursor.close()
    except Exception as error:
        print(error)
