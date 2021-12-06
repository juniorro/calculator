""" Testing Multiplication """
import datetime
import random
from calc.calculations.multiplication import Multiplication
from tests.file_util import get_csv_data, get_log_file_write

def test_calculation_multiplication():
    """ Testing static method for multiplication """
    #Arrange
    data = get_csv_data("multiplication.csv")
    mynumbers = tuple(data[0])
    #Act
    multiplication = Multiplication(mynumbers)
    #Assert
    get_log_file_write("multiplication_test.log", str(get_time()) + ",multiplication_test.py," + str(random.randint(10, 1000)) + ",multiplication," + str(multiplication.get_result()))
    assert multiplication.get_result() == 90000

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y:%H:%M:%S")
