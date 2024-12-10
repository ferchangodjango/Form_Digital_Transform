from models.entities.User import User
from flask import jsonify

#Implementando el repository
import DB.model as model
import DB.orm as orm
from DB.repository import Repository_Generic
from DB.config_connection import administrator_url
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
class ModelUser():

    @classmethod
    def LoggedUser(self,user):
        try:
            engine=create_engine(administrator_url)
            Session=sessionmaker(bind=engine)
            session=Session()
            orm.start_mappers_administrator()
            repositorio_general=Repository_Generic(session)
            answer=repositorio_general.get_username(user.username,model.Administrator)
            if answer !=None:
                user=User(answer.IDADMIN,answer.USERNAME,User.CheckPassword(answer.PASSWORD,user.password))
                return user
            
            else:
                return None
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod    
    def GetById(self,id):
        try:
            engine=create_engine(administrator_url)
            Session=sessionmaker(bind=engine)
            session=Session()
            repositorio_general=Repository_Generic(session)
            answer=repositorio_general.get_id(id,model.Administrator)
            if answer != None:
                user=User(answer.IDADMIN,answer.USERNAME,None)
                return user

            else:
                return None
        except Exception as ex:
            return Exception(ex)
    
    @classmethod
    def queryexecute(self,db,query):
        try:
            cursor=db.connection.cursor()
            cursor.execute(query)
            db.connection.commit()

            return jsonify({"message":"Insert data Ok!!"})
        
        except Exception as ex:
            raise Exception(ex)

        