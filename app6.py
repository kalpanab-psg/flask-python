# -*- coding: utf-8 -*-
"""
authour: bkalpana
In spyder type and the programrun directly after restarting kernel in console
"""
 

#Till now HTML inline coding done in return statements
#To use HTML file import  render function
#Create a templates folder and store html  files  
#
 
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def  index():
    return render_template("index1.html")
 

if __name__ == '__main__':
    app.run()
    
    
 