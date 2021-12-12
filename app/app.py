""" Web application entry point """
from flask import Flask, render_template, flash, request
from file_util import get_csv_data, get_log_file_write
app = Flask(__name__)
app.secret_key = '12111a9beb2bebab521d86cf113c9dafba6ab1ad'

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/calculator", methods=['GET'])
def calculator():
    return render_template('calculator.html')

@app.route("/result", methods=['GET'])
def result():
    file = get_csv_data("operation.csv")
    data = tuple(file)
    size = len(data)
    print(data)
    return render_template('result.html', size=size, data=data)

@app.route("/result", methods=['POST'])
def calculate():
    first_number = request.form['first-value']
    second_number = request.form['second-value']
    operation = request.form['operation']
    file = get_csv_data("operation.csv")
    data = tuple(file)
    size = len(data)
    get_log_file_write(str(first_number) +','+ str(second_number) +','+ str(operation) +','+ get_result(first_number, second_number, operation))
    return render_template('result.html', size=size, data=data)

def get_result(first_number, second_number, operation):
    first = float(first_number)
    second = float(second_number)
    return (float(first)) + (float(second))

# def get_result(first_number, second_number, operation):
    # match operation:
        # case 'addition':
            # return first_number + second_number
        # case 'substraction':
            # return first_number - second_number
        # case 'multiplication':
            # return first_number * second_number
        # case 'dividion':
            # return first_number / second_number
