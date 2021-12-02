""" Testing Division """
import datetime
import random
from calc.calculations.division import Division
from file_util import get_csv_data, get_log_file_write

def test_calculation_division():
    """ Testing static method for division """
    #Arrange
    data = get_csv_data("addition.csv")
    mynumbers = tuple(data)
    #Act
    division = Division(mynumbers)
    #Assert
    csvwriter = get_log_file_write("result.log")
    csvwriter.writerow(get_time(), "division_test", random.randint(10, 1000), "division", division.get_result())
    assert division.get_result() == 12

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
