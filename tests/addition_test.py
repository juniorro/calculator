""" Testing Addition """
import datetime
import random
from calc.calculations.addition import Addition
from tests.file_util import get_csv_data, get_log_file_write

def test_calculation_addition():
    """ Testing static method for addition """
    #Arrange
    data = get_csv_data("addition.csv")
    mynumbers = (tuple(data[0])[0], tuple(data[0])[1])
    #Act
    addition = Addition(mynumbers)
    #Assert
    get_log_file_write("addition_test.log", str(get_time()) + ",addition_test.py," + str(random.randint(10, 1000)) + ",addition," + str(addition.get_result()))
    assert addition.get_result() == 35

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y:%H:%M:%S")