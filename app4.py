# -*- coding: utf-8 -*-
"""
authour: bkalpana
In spyder type and the programrun directly after restarting kernel in console
"""
 
# Using redirect, url_for

# =============================================================================
# # 
# Flask class has a redirect() function. When called, it returns a response 
# object and redirects the user to another target location with specified
# status code.
# 
# Prototype of redirect() function is :
# Flask.redirect(location, statuscode, response)
# 
# url_for: To build a URL to a specific function, use the url_for() 
# function. It accepts the name of the function as its first argument and
# any number of keyword arguments, each corresponding to a variable part
# of the URL rule. Unknown variable parts are appended to the URL as query
# parameters.
# ref:https://flask.palletsprojects.com/en/1.1.x/quickstart/
# 
# =============================================================================

from flask import Flask, redirect ,url_for

app=Flask(__name__)

@app.route("/home")
def  home():
    return "<h1> Welcome to home page<h1>"
    
@app.route("/<name>")
def user(name):
    return f" <h2> Hello {name}!!. Welcome to flask programming.  <h2> "

@app.route("/admin")
def admin():
    return  redirect(url_for("home"))

if __name__ == '__main__':
    app.run()
    
    
     
# To run the progrm from spyder just run and type url:port no in browser
# example http://127.0.0.1:5000/home