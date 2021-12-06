""" Testing Subtraction """
import datetime
import random
from calc.calculations.subtraction import Subtraction
from tests.file_util import get_csv_data, get_log_file_write

def test_calculation_subtraction():
    """ Testing static method for subtraction """
    #Arrange
    data = get_csv_data("subtraction.csv")
    mynumbers = tuple(data[0])
    #Act
    subtraction = Subtraction(mynumbers)
    #Assert
    get_log_file_write("subtraction_test.log", str(get_time()) + ",subtraction_test.py," + str(random.randint(10, 1000)) + ",subtraction," + str(subtraction.get_result()))
    assert subtraction.get_result() == -116

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y:%H:%M:%S")
