from sqlalchemy import create_engine, text
from sqlalchemy import Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL


# Configurações
url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="$CF2246",
    host="localhost",
    port=3306,
    database="cinema"
)

engine = create_engine(url)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Filmes(Base):
    __tablename__ = "filmes"
    
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"[Filme: {self.titulo} | Gênero: {self.genero} | Ano de Lançamento: {self.ano}]"
    
# SQL

# INSERT
data_insert = Filmes(titulo= "Rambo II", genero= "Ação", ano= 1986)
session.add(data_insert)
session.commit()

# DELETE
# session.query(Filmes).filter(Filmes.titulo=="Batman").delete()
# session.commit()

# UPDATE
session.query(Filmes).filter(Filmes.genero=="Drama").update({"ano": 2015})
session.commit()

# SELECT
data = session.query(Filmes).all()
print(data)

session.close()


        