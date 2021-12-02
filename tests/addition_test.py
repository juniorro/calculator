""" Testing Addition """
import datetime
import random
from calc.calculations.addition import Addition
from file_util import get_csv_data, get_log_file_write

def test_calculation_addition():
    """ Testing static method for addition """
    #Arrange
    data = get_csv_data("addition.csv")
    mynumbers = tuple(data)
    #Act
    addition = Addition(mynumbers)
    #Assert
    csvwriter = get_log_file_write("result.log")
    csvwriter.writerow(get_time(), "addition_test", random.randint(10, 1000), "addition", addition.get_result())
    assert addition.get_result() == 35

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")