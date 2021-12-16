# REST != RESTFULL
# RESTFULL é um serviço web que ultiliza desse paradigma. 
# É ultilizada oara definir apop que implementr websservices qye yultilizam a arquitetura REST
# O uso Flask-restful acaba incentivando as práticas recomendadas oara a arquitetura com uma configuraçãi leve
from flask import Flask, request
import flask
import json
from flask_restful import Resource, Api


from introd_conceitos_api import desenvolvedor

app= Flask(__name__)
api = Api(app)

listaDev = [
    {   'id':0,
        'nome':'Vinicius',
        'habilidades':['Python','Flask']},
    {   'id':1,
        'nome':'Rafael',
        'habilidades':['Python','Django']}
]

class Desenvolvedor(Resource):
    def get(self,id):
        # Desta forma eu n preciso do jsonif para enviar meus json para a requisição
        try:
            response = listaDev[id]
            return response
        except IndexError:
            response = {'status':'excluido'}
            return response

    def put(self,id):
        dados=json.loads(request.data)
        listaDev[id] = dados
        return dados

    def delete(self,id):
        listaDev.pop(id)
        return {'status':'sucesso','mensagem':'registro excluido'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return listaDev
    def post(self):
        dados =json.loads(request.data)
        posicao = len(listaDev)
        dados['id'] = posicao
        listaDev.append(dados)
        return dados

api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/')
if __name__ == '__main__':
    app.run(debug=True)