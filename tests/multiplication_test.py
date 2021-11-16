""" Testing Multiplication """
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """ Testing static method for multiplication """
    #Arrange
    mynumbers = (2.0, 2.0)
    #Act
    multiplication = Multiplication(mynumbers)
    #Assert
    assert multiplication.get_result() == 4
