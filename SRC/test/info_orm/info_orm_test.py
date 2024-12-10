import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_login_excersice7/SRC')
import DB.model as model
import DB.orm as orm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,URL,text
import pandas as pd

"""Mybe this object need stay in management resources"""
url_object = URL.create(
    "mysql",
    username="root",
    password="89JQuery78#",
    host="localhost",
    database="papercompany")

engine=create_engine(url_object)
Session=sessionmaker(bind=engine)
session=Session()

mappers=orm.start_mappers()

#session.add(model.Sell(165,10,1,100))
#session.add(model.Sell(162,107,1,100))
#session.add(model.Sell(168,108,1,100))
#session.add(model.Sell(164,100,1,100))

row=list(session.execute(text("""SELECT sellers.NAME AS sellers,sum(products.PRODUCTPRICE*sells.QUANTITY)AS profit
                                FROM sells
                                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                                GROUP BY sellers
                                ORDER BY profit DESC""")))


#print(row)
#print(row2[-1])
#print(pd.DataFrame(row))

print(pd.DataFrame(row))
