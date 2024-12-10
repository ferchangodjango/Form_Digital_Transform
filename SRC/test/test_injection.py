import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_excericise_report/SRC/')

from DataAnalisys.Query import Query
from DB import ManageResources
from mysql.connector import Error
import mysql.connector 

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='question_data')
    cursor=connection.cursor()

    data={
        "COMPANY_NAME":str('EL_CRACK'),
        "QUESTION_A":10,
        "QUESTION_B":10,
        }
    query=Query.queryinsertPilot(data)
    print(query)
    cursor.execute(query)
    connection.commit()

except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conección a sido cerrada')

