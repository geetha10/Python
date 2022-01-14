from cmath import isnan
import re
from flask import Flask
print(__name__)
app =Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def sayDojo():
    return "Dojo!"

@app.route('/say/flask')
def sayFlask():
    return "Hi Flask!"

@app.route('/say/michael')
def sayMichael():
    return "Hi Michael!"

@app.route('/say/john')
def sayJohn():
    return "Hi John!"

@app.route('/say/<name>')
def sayName(name):
    return f"Hi {name[0].upper()+name[1:]}!"

@app.route('/repeat/<int:repeat_num>/<repeat_string>')
def repeat(repeat_num,repeat_string):
        return (repeat_string[0].upper()+repeat_string[1:]+" ")*repeat_num

if __name__=="__main__":     
    app.run(debug=True) 