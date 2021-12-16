from sqlalchemy.sql.sqltypes import String
from create_BD import Pessoas

def insere():
    name = str(input('Digite seu nome: '))
    years = int(input('Digite sua idade: '))
    pessoa = Pessoas(nome=name ,idade = years)
    print(pessoa)
    #commitando
    pessoa.save()#Methodo de commit feito em class Pessoas
def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome="Doguinho").first()
    # print(pessoa.idade)
def altera():
    pessoa = Pessoas.query.filter_by(nome='Doguinho').first()
    pessoa.nome = 'ASSIS'
    pessoa.save()
def exclui():
    pessoa = Pessoas.query.filter_by(nome='ASSIS').first()
    pessoa.delete()

if __name__=='__main__':
    # insere()
    # altera()
    exclui()
    consulta()
    