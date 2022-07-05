# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

# routes
@app.route('/add')
def perform_add():
    """add a and b params"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    ab_sum = operations.add(a,b)
    return f'{ab_sum}'

@app.route('/sub')
def perform_sub():
    """subtract a and b params"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    diff = operations.sub(a,b)
    return f'{diff}'

@app.route('/mult')
def perform_mult():
    """multiply a and b params"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = operations.mult(a,b)
    return f'{product}'

@app.route('/div')
def perform_div():
    """divide a and b params"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    quotient = operations.div(a,b)
    return f'{quotient}'