from wtforms import Form
from wtforms import IntegerField,validators,StringField,SelectField,FieldList,FormField
from mysql.connector import Error
import mysql.connector 
import pandas as pd



class Questions(Form):
    COMPANY_NAME=StringField("COMPANY_NAME")
    QUESTION_A=IntegerField("QUESTION_A",[validators.NumberRange(min=1,max=10)])
    QUESTION_B=IntegerField("QUESTION_B",[validators.NumberRange(min=1,max=10)])
    QUESTION_C=IntegerField("QUESTION_C",[validators.NumberRange(min=1,max=10)])
    QUESTION_D=IntegerField("QUESTION_D",[validators.NumberRange(min=1,max=10)])
    QUESTION_E=IntegerField("QUESTION_E",[validators.NumberRange(min=1,max=10)])
    QUESTION_F=IntegerField("QUESTION_F",[validators.NumberRange(min=1,max=10)])
    QUESTION_G=IntegerField("QUESTION_G",[validators.NumberRange(min=1,max=10)])
    QUESTION_H=IntegerField("QUESTION_H",[validators.NumberRange(min=1,max=10)])
    QUESTION_I=IntegerField("QUESTION_I",[validators.NumberRange(min=1,max=10)])
    QUESTION_J=IntegerField("QUESTION_J",[validators.NumberRange(min=1,max=10)])
    QUESTION_K=IntegerField("QUESTION_K",[validators.NumberRange(min=1,max=10)])
    QUESTION_L=IntegerField("QUESTION_L",[validators.NumberRange(min=1,max=10)])
    QUESTION_M=IntegerField("QUESTION_M",[validators.NumberRange(min=1,max=10)])
    QUESTION_O=IntegerField("QUESTION_O",[validators.NumberRange(min=0,max=1)])
    QUESTION_P=IntegerField("QUESTION_P",[validators.NumberRange(min=0,max=1)])
    QUESTION_Q=IntegerField("QUESTION_Q",[validators.NumberRange(min=0,max=1)])
    QUESTION_R=IntegerField("QUESTION_R",[validators.NumberRange(min=0,max=1)])
    QUESTION_S=IntegerField("QUESTION_S",[validators.NumberRange(min=0,max=1)])
    QUESTION_T=IntegerField("QUESTION_T",[validators.NumberRange(min=0,max=1)])
    QUESTION_U=IntegerField("QUESTION_U",[validators.NumberRange(min=0,max=1)])
    QUESTION_V=IntegerField("QUESTION_V",[validators.NumberRange(min=0,max=100)])



class IMForm(Form):
    try:
        connection=mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='89JQuery78#',
            db='question_data')
        cursor=connection.cursor()

        query="""SELECT *
                    FROM QUESTIONNAIRE_VALUES"""
        cursor.execute(query)
        answer=cursor.fetchall()
        DataFrameAnswer=pd.DataFrame(answer)

    except Exception as ex:
        raise Exception(ex)

    finally:
        if connection.is_connected():
            connection.close()
            
    Default_value=["Selecciona una empresa"]
    unique_names=Default_value+list(DataFrameAnswer[1])
    protocol = SelectField("protocol",
                           choices=[(i,i) for i in unique_names])
    username = StringField()

class ContactForm(Form):
    first_name  = StringField()
    last_name   = StringField()
    im_accounts = FieldList(FormField(IMForm))
