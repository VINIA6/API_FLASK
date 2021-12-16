#Verremos como implementar uma API para inclusçao de novos desenvolvedores e seus conhecimentos
#Iremos manipular uma lista que irá conectar o nome do desenvolvedor e suas habilidades(linguagem que domina)
#Tudo isso será feito através de APIS

from flask import Flask, request
from flask.json import jsonify
import json

app = Flask(__name__)

listaDev = [
    {   'id':0,
        'nome':'Vinicius',
        'habilidades':['Python','Flask']},
    {   'id':1,
        'nome':'Rafael',
        'habilidades':['Python','Django']}
]

@app.route('/dev/<int:id>/',methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = listaDev[id]
            return jsonify(response)
        except IndexError:
            response = {'status':'excluido'}
            return jsonify(response)
            
    elif request.method == 'PUT':
        dados=json.loads(request.data)
        listaDev[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        listaDev.pop(id)
        return jsonify({'status':'sucesso','mensagem':'registro excluido'})

@app.route('/dev/',methods=['POST','GET'])
def listaDesenvolvedor():
    if request.method == 'POST':
        dados =json.loads(request.data)
        posicao = len(listaDev)
        dados['id'] = posicao
        listaDev.append(dados)
        return jsonify(dados)

    elif request.method == 'GET':
        return jsonify(listaDev)

if __name__ == '__main__':
    app.run(debug=True)