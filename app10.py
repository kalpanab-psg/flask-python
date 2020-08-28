# -*- coding: utf-8 -*-
"""
authour: bkalpana
In spyder type and the programrun directly after restarting kernel in console
"""
 

 
#To use HTML file import  render function
#Create a templates folder and store html  files  

###########################################################################
#def  a function for two app.routes
#set images in webpages using static folder
#store image in static folder and set path using url_for function.



##########################################################################


from flask import Flask, render_template

app=Flask(__name__)

@app.route("/home")
@app.route("/")   # for both app.route run index()
def  index():
    return render_template("index5.html")
 
 


if __name__ == '__main__':
    app.run()
    
    
 