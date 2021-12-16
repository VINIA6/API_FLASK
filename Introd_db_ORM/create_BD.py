#Veremos banco de dados sqlite 
#Como criar um banco de dados sqlalchemy(ORM)
#Realizar operação de banco de dados(insret,update,select e delete
from sqlalchemy import create_engine, Column,Integer,String,ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey


# criando banco
engine = create_engine('sqlite:///teste.db',convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# criando tabela 
class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer,primary_key=True)
    nome = Column(String(40),index=True)
    idade = Column(Integer)
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)
    def save(self):
        db_session.add(self)
        db_session.commit()
    def delete(self):
        db_session.delete(self)
        db_session.commit()
class Atividades(Base):
    __tablename__='atividade'
    id = Column(Integer,primary_key=True)
    nome = Column(String(80))
    # chave estrangeira, iremos relacionar atividades com pessoa
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

#Inicializando banco
def init_db():
    Base.metadata.create_all(bind=engine)


if __name__=='__main__':
    init_db()


    

