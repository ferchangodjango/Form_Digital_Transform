from mysql.connector import Error
import mysql.connector 

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='89JQuery78#',
        db='question_data')
    QUERY_CREATION=""" CREATE TABLE QUESTIONNAIRE_VALUES(
                        ID_GLOBAL INT NOT NULL AUTO_INCREMENT,
                        COMPANY_NAME VARCHAR(45),
                        QUESTION_A INT,
                        QUESTION_B INT,
                        QUESTION_C INT,
                        QUESTION_D INT,
                        QUESTION_E INT,
                        QUESTION_F INT,
                        QUESTION_G INT,
                        QUESTION_H INT,
                        QUESTION_I INT,
                        QUESTION_J INT,
                        QUESTION_K INT,
                        QUESTION_L INT,
                        QUESTION_M INT,
                        QUESTION_O INT,
                        QUESTION_P INT,
                        QUESTION_Q INT,
                        QUESTION_R INT,
                        QUESTION_S INT,
                        QUESTION_T INT,
                        QUESTION_U INT,
                        QUESTION_V INT,
                        PRIMARY KEY(ID_GLOBAL))"""
    cursor=connection.cursor()
    cursor.execute(QUERY_CREATION)
    
except Exception as ex:
    raise Exception(ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conección a sido cerrada')