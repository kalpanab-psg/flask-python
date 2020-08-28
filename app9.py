# -*- coding: utf-8 -*-
"""
authour: bkalpana
In spyder type and the programrun directly after restarting kernel in console
"""
 

 
#To use HTML file import  render function
#Create a templates folder and store html  files  

###########################################################################

#to  send a listof values  in render prameter
# Check html index4.html


##########################################################################


from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def  index():
    return render_template("index4.html",content=['Aman','Bala', 'Abi', 'Saud'])
 
 


if __name__ == '__main__':
    app.run()
    
    
 