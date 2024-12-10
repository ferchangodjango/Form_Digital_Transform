from dataclasses import dataclass
from typing import NewType
from sqlalchemy.ext.instrumentation import InstrumentationManager
from sqlalchemy import Column,Integer,String,Table,MetaData,Float
from sqlalchemy.orm import registry
import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_login_excersice7/SRC')
from DB.config_connection import papercompany_url
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import class_mapper,clear_mappers
import pandas as pd
DEL_ATTR = object()

class FrozenDataclassInstrumentationManager(InstrumentationManager):
    """Management of events if a frozen data class (Father class)"""
    def install_member(self, class_, key, implementation):
        self.originals.setdefault(key, class_.__dict__.get(key, DEL_ATTR))
        setattr(class_, key, implementation)

    def uninstall_member(self, class_, key):
        original = self.originals.pop(key, None)
        if original is not DEL_ATTR:
            setattr(class_, key, original)
        else:
            delattr(class_, key)

    def dispose(self, class_):
        del self.originals
        delattr(class_, "_sa_class_manager")
    
    def manager_getter(self, class_):
        def get(cls):
            return cls.__dict__["_sa_class_manager"]
        return get

    def manage(self, class_, manager):
        self.originals = {}
        setattr(class_, "_sa_class_manager", manager)

    def get_instance_dict(self, class_, instance):
        return instance.__dict__

    def install_state(self, class_, instance, state):
        instance.__dict__["state"] = state

    def remove_state(self, class_, instance, state):
        del instance.__dict__["state"]

    def state_getter(self, class_):
        def find(instance):
            return instance.__dict__["state"]
        return find

Reference=NewType("References",int)
ProductName=NewType("ProductName",str)
SellerName=NewType("SellerName",str)
LastName=NewType("LastName",str)
Email=NewType("Email",str)
UserName=NewType("UserName",str)
Password=NewType("Password",str)
Position=NewType("Position",str)
ProductPrice=NewType("ProductType",float)
Quantity=NewType("Quantity",int)

@dataclass(frozen=True)
class ProductNew:
    __sa_instrumentation_manager__ = FrozenDataclassInstrumentationManager
    IDPRODUCTS:int
    PRODUCTNAME:str
    PRODUCTPRICE:float

#@dataclass(frozen=True)
class Product:
    
    def __init__(self,IDPRODUCTS:Reference,PRODUCTNAME:ProductName,PRODUCTPRICE:ProductPrice) -> None:
        """This class is the model of the table product of the paper company"""
        self.IDPRODUCTS=IDPRODUCTS
        self.PRODUCTNAME=PRODUCTNAME
        self.PRODUCTPRICE=PRODUCTPRICE
    
    #__sa_instrumentation_manager__ = FrozenDataclassInstrumentationManager


mapper_registry = registry()

metadata=MetaData()

product_table=Table(
    "products",
    metadata,
    Column('IDPRODUCTS',Integer,primary_key=True,autoincrement=True),
    Column('PRODUCTNAME',String(255)),
    Column('PRODUCTPRICE',Float)
)

product_table_is_the_same=Table(
    "products",
    metadata,
    Column('IDPRODUCTS',Integer,primary_key=True,autoincrement=True),
    Column('PRODUCTNAME',String(255)),
    Column('PRODUCTPRICE',Float),
    extend_existing=True
)

def get_list_tuples(list_objects:list[object]) -> list:
    list_tuples=[]
    try:
        
        for i in range(len(list_objects)):
            tuple_object=(list_objects[i].IDPRODUCTS,list_objects[i].PRODUCTNAME,list_objects[i].PRODUCTPRICE)
            list_tuples.append(tuple_object)
        return list_tuples
    except Exception as ex:
        return list_tuples
    
products_mapper=mapper_registry.map_imperatively(Product,product_table)
engine=create_engine(papercompany_url)
Session=sessionmaker(bind=engine)
session=Session()
#print(list(session.query(Product).all()))
data_rowbyrow=get_list_tuples(list(session.query(Product).all()))
print(data_rowbyrow)
print(pd.DataFrame(data_rowbyrow))

#active_mapper=class_mapper(ProductNew)

metadata.clear()
mapper_registry.dispose()

products_mapper_new=mapper_registry.map_imperatively(Product,product_table)
#print(list(session.query(ProductNew).all()))