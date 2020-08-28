# -*- coding: utf-8 -*-
"""
authour: bkalpana
In spyder type and the programrun directly after restarting kernel in console
"""
 
# Using redirect, url_for with parameters
#redirecting using parameters 

 
from flask import Flask, redirect ,url_for

app=Flask(__name__)

@app.route("/home")
def  home():
    return "<h1> Welcome to home page<h1>"
    
@app.route("/<name>")
def user(name):
    return f" <h2> Hello {name}!!. Welcome to flask programming.  <h2> "

@app.route("/admin")
def admin():    #redirect to user function  with name as keyword parameter 
    return  redirect(url_for("user", name="Admin"))

if __name__ == '__main__':
    app.run()
    
    
 