import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_login_excersice7/SRC')
import DB.model as model
import DB.orm as orm
from DB.repository import Repository_Generic
from DB.config_connection import papercompany_url
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#Importacion de Querys
from DataAnalisys.Query import Query

engine=create_engine(papercompany_url)
Session=sessionmaker(bind=engine)
session=Session()

mappers=orm.start_mappers()

repositorio_general=Repository_Generic(session)
print(repositorio_general.QueryExecute(Query.queryprofitseller()))