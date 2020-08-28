# -*- coding: utf-8 -*-
"""
authour: bkalpana

"""
# =============================================================================
 
# pip install flask 
# pip list
# In spyder type  and run the program directly after restarting kernel in console
#
# if you want to run from windows terminal use EXPORT and run flask using
# python -m switch
#
# ref :  https://flask.palletsprojects.com/en/1.1.x/quickstart/

# =============================================================================

# Using  html  tags 

from flask import Flask

app=Flask(__name__)

@app.route("/home")
def index():
    return "<h1> Welcome to home page<h1>"
    
 
if __name__ == '__main__':
    app.run()
    
    
     
# To run the progrm from spyder just run and type url:port no in browser
# example http://127.0.0.1:5000/home