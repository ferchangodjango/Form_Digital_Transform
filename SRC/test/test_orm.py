import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_login_excersice7/SRC')
import DB.model as model
import DB.orm as orm
from sqlalchemy.orm import sessionmaker,class_mapper,clear_mappers,registry
from sqlalchemy import create_engine,URL,text
import pandas as pd
import pytest


@pytest.fixture
def connect_to_engine():
    """Mybe this object need stay in management resources"""
    url_object = URL.create(
        "mysql",
        username="root",
        password="89JQuery78#",
        host="localhost",
        database="papercompany")
    engine=create_engine(url_object)
    return engine

@pytest.fixture
def session(connect_to_engine):
    orm.start_mappers()
    yield sessionmaker(bind=connect_to_engine)()


@pytest.mark.parametrize(
        "idsell,idproducts,idseller,quantity",
        [(161,15,59,20)]
)
def test_add_object_to_tables(session,idsell,idproducts,idseller,quantity):

    """End Understand mapper"""
    sell_test=model.Sell(idsell,idproducts,idseller,quantity)
    session.add(sell_test)
    #session.commit()
    row=list(session.query(model.Sell).all())


    assert row[-1]==sell_test


