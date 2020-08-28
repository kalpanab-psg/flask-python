# -*- coding: utf-8 -*-
"""
authour: bkalpana
In spyder type and the programrun directly after restarting kernel in console
"""
 

 
#To use HTML file import  render function
#Create a templates folder and store html  files  
# pass value through render_template function as keyword parameter

 
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def  index():
    return render_template("index1.html")
 
@app.route("/<name>")
def  user(name):
    return render_template("index2.html", content=name)


if __name__ == '__main__':
    app.run()
    
    
 