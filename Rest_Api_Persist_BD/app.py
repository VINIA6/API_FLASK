from flask import Flask, app, request
from flask_restful import Resource, Api
from sqlalchemy.sql.expression import delete
from werkzeug.wrappers import response
from create_BD import Pessoas, Atividades

app=Flask(__name__)
api=Api(app)

# Lemnbrando que usaremos o método Restful

class Pessoa(Resource):
    def get(self,name):

        pessoa = Pessoas.query.filter_by(nome=name).first()

        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }

        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa não encontrada'
            }

        return response
    def post(self,name):

        pessoa = Pessoas.query.filter_by(nome=name).first()
        dados = request.json

        if'nome' in dados:
            pessoa.nome = dados['nome']
        if'idade' in dados:
            pessoa.idade = dados['idade']

        pessoa.save()

        response ={
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response
    def delete(self, name):

        pessoa = Pessoas.query.filter_by(nome=name).first()
        mensagem= 'Pessoa {} excluida com sucesso'.format(pessoa.nome)

        pessoa.delete()
        
        return {'status':'sucesso','mensagem':mensagem}
    

class ListaPessoas(Resource):
    def get(self):
        pessoa = Pessoas.query.all()
        # Lembrando que se for com um banco mt grande n devemos chamar tudo 
        response = [{"id":i.id,"nome":i.nome,"idade":i.idade} for i in pessoa]# for in line
        return response
    def post(self):
        dados = request.json

        pessoa = Pessoas(nome=dados['nome'],idade=dados['idade'])
        pessoa.save()

        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idades':pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        # Lembrando que se for com um banco mt grande n devemos chamar tudo 
        response = [{"id":i.id,"nome":i.nome,"pessoa":i.pessoa} for i in atividades]# for in line
        return response
    def post(self):
        dados=request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade= Atividades(nome=dados['nome'],pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response
api.add_resource(Pessoa, '/pessoa/<string:name>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades,'/atividades/')

if __name__ == '__main__':
    app.run(debug=True)