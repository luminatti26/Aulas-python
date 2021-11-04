'''projeto de adoção

1 - cadastro de pessoas
2 - cadastro de pets (caso seja para doar um pet)
3 - selecionar um pet (caso seja para adotar um pet)

'''
from flask import Flask, render_template, request, redirect
from repositorio import cadastro_cliente_db, visualizar_clientes_db, alterar_clientes_db, deletar_clientes_db, selecionar_clientes
from repositorio import conexao, cadastro_pet_db, visualizar_pet_db, alterar_pet_db, deletar_pet_db, selecionar_pet_db

projeto = Flask(__name__)

@projeto.route("/")
def pag_inicial():
    db = conexao()
    lista_pet = visualizar_pet_db(db)
    return render_template("index.html", lista_pet_db= lista_pet)


@projeto.route("/cadastro")
def pag_cadastro():
    return render_template("/cadastro.html") 


@projeto.route("/doação")
def pag_doacao():
    db = conexao()
    lista_pet = visualizar_pet_db(db)
    return render_template("/doação.html", lista_pet_db= lista_pet)


@projeto.route("/clientes")
def pag_clientes():
    db = conexao()
    lista_clientes = visualizar_clientes_db(db)
    return render_template("/clientes.html", lista_clientes_db= lista_clientes)
    

@projeto.route("/salvar/cliente", methods=["POST"])
def salvar_cliente():
    db = conexao()
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    cadastro_cliente_db(db, nome, sobrenome, cpf, telefone)
    return redirect("/clientes")


projeto.run(debug=True)
