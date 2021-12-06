""" Testing Division """
import datetime
import random
from calc.calculations.division import Division
from tests.file_util import get_csv_data, get_log_file_write

def test_calculation_division():
    """ Testing static method for division """
    #Arrange
    data = get_csv_data("division.csv")
    mynumbers = tuple(data[0])
    #Act
    division = Division(mynumbers)
    #Assert
    get_log_file_write("result.log", str(get_time()) + "division_test" + str(random.randint(10, 1000)) + "division" + str(division.get_result()))
    assert division.get_result() == 20

def get_time():
    return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
