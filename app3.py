'''
authour : bkalpana
In spyder type  & run programdirectly after restarting kernel in console
'''


#  =============================================================================
#  
# # Using  html  tags and variable names
# Variable Rules
# You can add variable sections to a URL by marking sections 
# with <variable_name>. Your function then receives the <variable_name>
# as a keyword argument. Optionally, you can use a converter to specify 
# the type of the argument like <converter:variable_name>.
# 
# converter can be:    string, int, float, uuid,path
#
# =============================================================================



from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1> Welcome to home page<h1>"
    
@app.route("/<name>")
def user(name):
    return f" <h2> Hello {name}!!. Welcome to flask programming.  <h2> "

if __name__ == '__main__':
    app.run()
    
    
     
# To run the progrm from spyder just run and type url:port no in browser
# example http://127.0.0.1:5000/