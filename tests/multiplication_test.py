""" Testing Multiplication """
import datetime
import random
from calc.calculations.multiplication import Multiplication
from file_util import get_csv_data, get_log_file_write

def test_calculation_multiplication():
    """ Testing static method for multiplication """
    #Arrange
    data = get_csv_data("multiplication.csv")
    mynumbers = tuple(data)
    #Act
    multiplication = Multiplication(mynumbers)
    #Assert
    csvwriter = get_log_file_write("result.log")
    csvwriter.writerow(get_time(), "multiplication_test", random.randint(10, 1000), "multiplication", multiplication.get_result())
    assert multiplication.get_result() == 300

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
