# -*- coding: utf-8 -*-
"""
authour: bkalpana
In spyder type and the programrun directly after restarting kernel in console
"""
 

 
#To use HTML file import  render function
#Create a templates folder and store html  files  

###########################################################################

#to use a for , if statements  in html file write python code inside {%  %}
# Check html index3.html


##########################################################################


from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def  index():
    return render_template("index3.html",val=7)
 
 


if __name__ == '__main__':
    app.run()
    
    
 