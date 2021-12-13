""" Web application entry point """
from flask import Flask, render_template, flash, request, flash, redirect, url_for
from file_util import get_csv_data, write_to_file
app = Flask(__name__)
app.secret_key = '12111a9beb2bebab521d86cf113c9dafba6ab1ad'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET'])
def calculator():
    return render_template('calculator.html')

@app.route('/result', methods=['POST'])
def calculate():
    first_number = request.form['first-value']
    second_number = request.form['second-value']
    operation = request.form['operation']
    if(first_number and second_number and operation):
        dataframe = [[first_number, second_number, operation, get_result(first_number, second_number, operation)]]
        write_to_file(dataframe)
        file = get_csv_data('operation.csv')
        data = tuple(file)
        size = len(data)
        return render_template('result.html', size=size, data=data)
    else:
        flash('Please enter 2 numbers and an operation')
        return redirect(url_for('calculator'))

@app.route('/history', methods=['GET'])
def history():
    file = get_csv_data('operation.csv')
    data = tuple(file)
    size = len(data)
    return render_template('result.html', size=size, data=data)

def get_result(first_number, second_number, operation):
    first = float(first_number)
    second = float(second_number)
    if(operation == 'addition'):
            return first + second
    elif(operation == 'subtraction'):
            return first - second
    elif(operation == 'multiplication'):
            return first * second
    else:
        return first / second

@app.errorhandler(ZeroDivisionError)
def handle_error(exception):
    flash('Cannot divide by 0. You know that. Please try again.')
    return redirect(url_for('calculator'))
