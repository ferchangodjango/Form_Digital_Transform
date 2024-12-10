import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_login_excersice7/SRC')
import DB.model as model
import DB.orm as orm
from DB.repository import Repository_Generic
from DB.config_connection import administrator_url
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#Importacion de Querys
from DataAnalisys.Query import Query

engine=create_engine(administrator_url)
Session=sessionmaker(bind=engine)
session=Session()

orm.start_mappers_administrator()

repositorio_general=Repository_Generic(session)
list_keys=repositorio_general.get_username('ELGORDOTONY',model.Administrator)
list_id=repositorio_general.get_id(1,model.Administrator)
print(list_id)