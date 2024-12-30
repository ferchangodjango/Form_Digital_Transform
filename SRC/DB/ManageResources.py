from flask import jsonify
import pandas as pd
from bokeh.embed import components
from bokeh.resources import INLINE
import random
import numpy as np

class ManageResources():
    @classmethod
    def queryExecute(self,db,query,insert=False):
        """ This function in case than insert is false only execute a Query, and return a 
        DataFrame with the values of Query, the arguments are the data base
        and the Query than need to execute, id insert isn´t false only execute the Query"""
        try:
            #get the connection
            cursor=db.connection.cursor()
            cursor.execute(query)
            if insert==False:
                #get the DataFrame
                answer=cursor.fetchall()
                answerDataFrame=pd.DataFrame(answer)
                db.connection.commit()
                return answerDataFrame
            else:
                db.connection.commit()
                return jsonify({"mesage":"Insert data Ok!"})
            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def extractResource(self,graph):
        """ This function is for extract the script, div, JS_resources and CSS_resources
        from bokeh graphs, for can render in the diferentes templates, you only need to pass
        the graph than you want extract the resources."""
        script,div=components(graph)
        js_resources=INLINE.render_js()
        css_resources=INLINE.render_css()
        data={
            "script":script,
            "div":div,
            "js_resources":js_resources,
            "css_resources":css_resources
        }
        return data
    
    @classmethod
    def extractResourceTheme(self,graph,theme=None):
        """ This function is for extract the script, div, JS_resources and CSS_resources
        from bokeh graphs, for can render in the diferentes templates, but in this case, this
        function have the functionality to can add the theme"""
        if theme==None:
            script,div=components(graph)
        else:
            script,div=components(graph,theme=theme)
        js_resources=INLINE.render_js()
        css_resources=INLINE.render_css()
        data={
            "script":script,
            "div":div,
            "js_resources":js_resources,
            "css_resources":css_resources
        }
        return data
    
    
    @classmethod
    def joinDictionary(self,dictionary_list):
        """
        This function Join a list of dictionary for create a 
        big dictionary than can render in the HTML templates, specific a dictionary
        with this keys:
        data={
            "script":script,
            "div":div,
            "js_resources":js_resources,
            "css_resources":css_resources
        } 
        This function is specific for join this kind of dictionary
        """
        keys_list=list(dictionary_list[0].keys())
        for i in range(len(dictionary_list)):
            for j in keys_list:
                dictionary_list[i][j+str(i+1)]=dictionary_list[i].pop(j)
        dictionary_master={}
        for i in range(len(dictionary_list)):
            dictionary_master=dictionary_master|dictionary_list[i]
        return dictionary_master

    @classmethod
    def changeName(self,data,*args):
        """
        This function changes the name from the data frame,and return a new data with the name
        changed, the argumentes than need is the data, and the names
        """
        columnsName=list(data.columns)
        for i in range(len(args)):
            data=data.rename(columns={columnsName[i]:args[i]})
        return data
    
    @classmethod
    def concatColumns(self,data):
        names=list(data.columns)
        datas=[]
        for i in range(len(names)):
            newData=pd.DataFrame(data.loc[:,names[i]])
            newData=newData.rename(columns={names[i]:"Values"})
            newData["Name"]=names[i]
            datas.append(newData)
        dataConcat=pd.concat(datas)
        dataConcat=dataConcat.reset_index(drop=True)
        return dataConcat
            
