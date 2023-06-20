#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<str>')
def print_string(str):
    print (str)
    return str

#@app.route("/count/<int:num>")
#def count (num):
   # result =''
    #for i in range(num+1):
       # result += str(i)+'\n '
        #return result
    
@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(parameter + 1))
    return numbers

@app.route("/math/int:<num1>/<operation>/int:<num2>") 
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
        return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
