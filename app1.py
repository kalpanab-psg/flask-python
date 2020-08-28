# -*- coding: utf-8 -*-
"""
First python flask program
project:flask_program1
"""
# =============================================================================
# 
# install python
# create a new Environment -flask 
# activate Environment 
# pip install flask 
# pip list
# In spyder type the program and run directly


# =============================================================================


from flask import Flask

# configuration
DEBUG = True

app=Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the index page"
    
@app.route("/hi/")
def who():
    return "Who are you?"
    
@app.route("/hi/<username>")
def greet(username):
    return "Hello. Welcome {username}!!"


if __name__ == '__main__':
    app.run()
    #app.run(host="localhost", port=int("777")) # specify port number of choice