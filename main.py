import mysql.connector
from flask import Flask, jsonify, make_response, request
# from bd import Carros

mydb = mysql.connector.connect(
    host='localhost',
    user='user',
    password='123456',
    database='DbCarros'
)

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/carros", methods=["GET"])
def get_carros():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM Carros')
    meus_carros = my_cursor.fetchall()

    carros = list()
    for carro in meus_carros:
        carros.append(
            {
                'id': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3]
            }
        )

    return carros


@app.route("/carros", methods=["POST"])
def create_carro():
    carro = request.json

    my_cursor = mydb.cursor()
    sql = f"""INSERT INTO Carros (marca, modelo, ano)
         VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"""
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(mensagem="Carro cadastrado com sucesso!!!",
                carro=carro,
        )
    )


@app.route("/carros/<int:id>", methods=["DELETE"])
def delete_carro(id):
    my_cursor = mydb.cursor()
    sql = f"DELETE FROM Carros WHERE id = {id}"
    my_cursor.execute(sql)
    mydb.commit()

    if my_cursor.rowcount:
        return make_response(jsonify(mensagem="Carro removido com sucesso!"),
                             200)
    else:
        return make_response(jsonify(mensagem="Carro não encontrado!"), 404)



@app.route("/carros/<int:id>", methods=["PATCH"])
def update_carro(id):
    carro_to_update = None
    for carro in Carros:
        if carro['id'] == id:
            carro_to_update = carro
            break

    if carro_to_update:
        data = request.json
        for key, value in data.items():
            carro_to_update[key] = value
        return make_response(
            jsonify(mensagem="Carro atualizado com sucesso!",
                    carro=carro_to_update),
            200,
        )
    else:
        return make_response(jsonify(mensagem="Carro não encontrado!",
                                     carro=None), 404)


app.run()
