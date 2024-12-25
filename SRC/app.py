from flask import Flask,render_template,request,redirect,url_for
from config import ConfigObject
from flask_mysqldb import MySQL
from models.forms import Questions
from DataAnalisys.Query import Query
from DataAnalisys.DigitalTransformReport import ResumeFormDigitalTransform
from DataAnalisys.dinamicGraphs import RadarChart
from DB.ManageResources import ManageResources

app=Flask(__name__)
db=MySQL(app)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def index():
    return redirect(url_for('insertsell'))


@app.route('/insertsell',methods=['GET','POST'])
def insertsell():
    """This Function get the data throuht a form,
    In efect, is only a view about a simple form"""
    formulario=Questions()
    if request.method=='POST':
        data={
            "COMPANY_NAME":request.form['COMPANY_NAME'],
            "QUESTION_A":request.form['QUESTION_A'],
            "QUESTION_B":request.form['QUESTION_B'],
            "QUESTION_C":request.form['QUESTION_C'],
            "QUESTION_D":request.form['QUESTION_D'],
            "QUESTION_E":request.form['QUESTION_E'],
            "QUESTION_F":request.form['QUESTION_F'],
            "QUESTION_G":request.form['QUESTION_G'],
            "QUESTION_H":request.form['QUESTION_H'],
            "QUESTION_I":request.form['QUESTION_I'],
            "QUESTION_J":request.form['QUESTION_J'],
            "QUESTION_K":request.form['QUESTION_K'],
            "QUESTION_L":request.form['QUESTION_L'],
            "QUESTION_M":request.form['QUESTION_M'],
            "QUESTION_O":request.form['QUESTION_O'],
            "QUESTION_P":request.form['QUESTION_P'],
            "QUESTION_Q":request.form['QUESTION_Q'],
            "QUESTION_R":request.form['QUESTION_R'],
            "QUESTION_S":request.form['QUESTION_S'],
            "QUESTION_T":request.form['QUESTION_T'],
            "QUESTION_U":request.form['QUESTION_U'],
            "QUESTION_V":request.form['QUESTION_V']
        }
        query=Query.queryinsert(data)
        insert_data=ManageResources.queryExecute(db,query,insert=True)

        return render_template('CRUD/insertsell.html',data=data,form=formulario)
    else:
        data={
            "IDPRODUCT":1,
            "IDSELLERS":1,
            "QUANTITY":1

        }
        return render_template('CRUD/insertsell.html',data=data,form=formulario)

@app.route('/GetResources',methods=['GET'])
def GetResources():
    query=Query.consultingData()
    DataFramePilot=ManageResources.queryExecute(db,query)
    DataResumePilot=ResumeFormDigitalTransform(DataFramePilot,'VEQ3')
    MainRadarGraph=RadarChart(DataResumePilot)
    MainRadarResources=ManageResources.extractResource(MainRadarGraph)

    return (render_template('CRUD/GetData.html', data=MainRadarResources))



if __name__=='__main__':
    app.config.from_object(ConfigObject)
    app.run()