""" Web application entry point """
from flask import Flask, render_template, flash, request

app = Flask(__name__)
# app.run(debug=True, use_debugger=False, use_reloader=True)
app.secret_key = '12111a9beb2bebab521d86cf113c9dafba6ab1ad'

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/calculator", methods=['GET'])
def calculator():
    return render_template('index.html')

@app.route("/calculate", methods=['POST'])
def calculate():
    first_number = request.form['first-value']
    second_number = request.form['second-value']
    operation = request.form['operation']
    print(first_number)
    print(second_number)
    print(operation)
    return render_template('index.html')
