""" Testing Addition """
from calc.calculations.addition import Addition
from file_util import get_csv_data, get_log_file_write

def test_calculation_addition():
    """ Testing static method for addition """
    #Arrange
    data = get_csv_data("addition.csv")
    for row in data:
        mynumbers = tuple(value)
        print(mynumbers)
        #Act
        addition = Addition(mynumbers)
        #Assert
        csvwriter = get_log_file_write("result.log")
        csvwriter.writerow(row, addition.get_result())
        # assert addition.get_result() == 9.0
        assert 0.9 == 9.0
