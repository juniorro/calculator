""" Testing Subtraction """
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """ Testing static method for subtraction """
    #Arrange
    mynumbers = (5.0, 2.0)
    #Act
    subtraction = Subtraction(mynumbers)
    #Assert
    assert subtraction.get_result() == -7
