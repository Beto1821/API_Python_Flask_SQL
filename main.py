from flask import Flask, request
from bd import Carros

app = Flask(__name__)


@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros


@app.route('/carros', methods=['POST'])
def create_car():
    carro = request.json
    Carros.append(carro)
    return Carros


app.run()
