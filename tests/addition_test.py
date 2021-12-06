""" Testing Addition """
import datetime
import random
from calc.calculations.addition import Addition
from tests.file_util import get_csv_data, get_log_file_write

def test_calculation_addition():
    """ Testing static method for addition """
    #Arrange
    data = get_csv_data("addition.csv")
    mynumbers = tuple(data[0])
    #Act
    addition = Addition(mynumbers)
    #Assert
    get_log_file_write("result.log", str(get_time()) + "addition_test" + str(random.randint(10, 1000)) + "addition" + str(addition.get_result()))
    assert addition.get_result() == 70

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")