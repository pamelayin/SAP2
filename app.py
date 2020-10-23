from jinja2 import environment
import math
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:number>')
def readAll(number):
    try:
        return render_template('integers.html', number = number)
    except Exception as e:
        return str(e)

@app.route('/<int:number>/odd')
def readOdd(number):
    try:
        return render_template('odd.html', number = number)
    except Exception as e:
        return str(e)

@app.route('/<int:number>/even')
def readEven(number):
    try:
        return render_template('even.html', number = number)
    except Exception as e:
        return str(e)

@app.route('/<int:number>/prime')
def readPrime(number):
    try:
        return render_template('prime.html', number = number)
    except Exception as e:
        return str(e)

#prime number filter
def is_prime(number):
    if number == 2:
        return True
    for i in range(2, number):
        if (number % i == 0):
            return False;
        return True
app.jinja_env.tests['prime'] = is_prime

if __name__ == "__main__":
    app.run(debug=True)