import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_excericise_report/SRC/')

from DataAnalisys.Query import Query
from DB import ManageResources
from mysql.connector import Error
import mysql.connector 
import pandas as pd

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='question_data')
    cursor=connection.cursor()

    query=Query.consultingData()
    cursor.execute(query)
    answer=cursor.fetchall()
    DataFrameAnswer=pd.DataFrame(answer)
    print(DataFrameAnswer)

except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conección a sido cerrada')
