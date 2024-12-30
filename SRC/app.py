from flask import Flask,render_template,request,redirect,url_for
from config import ConfigObject
from flask_mysqldb import MySQL
from models.forms import Questions, IMForm
from DataAnalisys.Query import Query
from DataAnalisys.DigitalTransformReport import ResumeFormDigitalTransform
from DataAnalisys.dinamicGraphs import RadarChart,ParetoDinamicColors
from DB.ManageResources import ManageResources
from bokeh.io import curdoc
from bokeh.themes import Theme
import os

#Forms
from wtforms import Form
from wtforms import SelectField

#Get the main path for reference the several file paths
main_path=os.getcwd()

#Start the aplication
app=Flask(__name__)
#Add the SQL Server for do the queries
db=MySQL(app)


@app.route('/home')
def home():
    """This function only redirect the main page"""
    return render_template('home.html')

@app.route('/')
def index():
    """This function redirect always to the home"""
    return redirect(url_for('home'))


@app.route('/digital_maturity_form',methods=['GET','POST'])
def digital_maturity_form():
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

        return render_template('CRUD/digital_maturity_form.html',form=formulario)
    else:
        return render_template('CRUD/digital_maturity_form.html',form=formulario)

@app.route('/GetResources',methods=['GET','POST'])
def GetResources():
    """This view redirect to the a little dashboard for get the information
    about the diferent companies than fill the form"""
    main_theme=curdoc()
    TransparencyTheme=Theme(os.path.join(main_path,"SRC","static","ThemesCustom","TransparencyTotal.yml"))
    main_theme.theme = TransparencyTheme
    
    query=Query.consultingData()
    RAW_QUERY=ManageResources.queryExecute(db,query)
    Unique_Posibilitieslist=list(RAW_QUERY[1])
    class SelectionForm(Form):
        Default_value=["Selecciona una empresa"]
        unique_names=Default_value+Unique_Posibilitieslist
        protocol = SelectField("protocol",
                            choices=[(i,i) for i in unique_names])
    formulario=SelectionForm()
    
    if request.method=='POST':
        data={

            "Answer":request.form['protocol']
        }
        
        
        if data["Answer"] in Unique_Posibilitieslist:

            RESUMEN_DIGITAL_TEST=ResumeFormDigitalTransform(RAW_QUERY,data["Answer"])
            
            #Get the data.
            MainRadarGraph=RadarChart(RESUMEN_DIGITAL_TEST)
            MainParetoGraph=ParetoDinamicColors(RESUMEN_DIGITAL_TEST,"CATEGORY","REAL %")
            
            #Get the resources
            MainRadarResources=ManageResources.extractResourceTheme(MainRadarGraph,theme=main_theme.theme)
            MainParetoResources=ManageResources.extractResourceTheme(MainParetoGraph,theme=main_theme.theme)

            #Make a resources list
            resources_list=[MainRadarResources,MainParetoResources]

            #Join the resouces list
            data=ManageResources.joinDictionary(resources_list)
            return (render_template('CRUD/GetData.html', data=data, form=formulario))
        else:
            RESUMEN_DIGITAL_TEST=ResumeFormDigitalTransform(RAW_QUERY,'VEQ3')
            
            #Get the data
            MainRadarGraph=RadarChart(RESUMEN_DIGITAL_TEST)
            MainParetoGraph=ParetoDinamicColors(RESUMEN_DIGITAL_TEST,"CATEGORY","REAL %")
            
            #Get the resources
            MainRadarResources=ManageResources.extractResourceTheme(MainRadarGraph,theme=main_theme.theme)
            MainParetoResources=ManageResources.extractResourceTheme(MainParetoGraph,theme=main_theme.theme)

            #Make a resources list
            resources_list=[MainRadarResources,MainParetoResources]

            #Join the resouces list
            data=ManageResources.joinDictionary(resources_list)
            return (render_template('CRUD/GetData.html', data=data, form=formulario))


    else:
        RESUMEN_DIGITAL_TEST=ResumeFormDigitalTransform(RAW_QUERY,'VEQ3')

        #Get the graphs
        MainRadarGraph=RadarChart(RESUMEN_DIGITAL_TEST)
        MainParetoGraph=ParetoDinamicColors(RESUMEN_DIGITAL_TEST,"CATEGORY","REAL %")
        
        #Get the resources
        MainRadarResources=ManageResources.extractResourceTheme(MainRadarGraph,theme=main_theme.theme)
        MainParetoResources=ManageResources.extractResourceTheme(MainParetoGraph,theme=main_theme.theme)

        #Make a resources list
        resources_list=[MainRadarResources,MainParetoResources]

        #Join the resouces list
        data=ManageResources.joinDictionary(resources_list)
        return (render_template('CRUD/GetData.html', data=data, form=formulario))



if __name__=='__main__':
    app.config.from_object(ConfigObject)
    app.run()