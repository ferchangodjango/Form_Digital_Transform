from mysql.connector import Error
import mysql.connector 

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='question_data')
    QUERY_CREATION=""" CREATE TABLE QUESTIONNAIRE_FIX(
                        ID_GLOBAL INT NOT NULL AUTO_INCREMENT,
                        COMPANY_NAME CHAR(255),
                        QUESTION_A INT,
                        QUESTION_B INT,
                        PRIMARY KEY(ID_GLOBAL))"""
    cursor=connection.cursor()
    cursor.execute(QUERY_CREATION)
    
except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conección a sido cerrada')