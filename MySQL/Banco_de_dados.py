import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database='apostila',
    user='root',
    password='lucas26'
)


try:
    cursor = db.cursor()
    print('conectou no banco')
    sql ='select * from pessoa'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for index in resultado:
        print(index[0], index[1])
    cursor.close()
except Exception as error:
    print(error)

try:
    cursor = db.cursor()
    print('conectou no banco')
    sql = 'update pessoa set nome = %s where nome = %s'
    parametros = ('Pedro', 'Lucas Minatti')
    cursor.execute(sql, parametros)
    db.commit()
    cursor.close()
except Exception as error:
    print(error)

try:
    cursor = db.cursor()
    print('conectou no banco')
    nome = 'Pedro'
    sql = f'delete from pessoa where nome = "{nome}"'
    cursor.execute(sql)
    db.commit()
    cursor.close()
except Exception as error:
    print(error)





