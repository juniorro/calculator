""" Testing Subtraction """
import datetime
import random
from calc.calculations.subtraction import Subtraction
from file_util import get_csv_data, get_log_file_write

def test_calculation_subtraction():
    """ Testing static method for subtraction """
    #Arrange
    data = get_csv_data("subtraction.csv")
    mynumbers = tuple(data)
    #Act
    subtraction = Subtraction(mynumbers)
    #Assert
    csvwriter = get_log_file_write("result.log")
    csvwriter.writerow(get_time(), "subtraction_test", random.randint(10, 1000), "subtraction", subtraction.get_result())
    assert subtraction.get_result() == 44

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
