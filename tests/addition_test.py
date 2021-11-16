""" Testing Addition """
from calc.calculations.addition import Addition

def test_calculation_addition():
    """ Testing static method for addition """
    #Arrange
    mynumbers = (1.0, 8.0)
    #Act
    addition = Addition(mynumbers)
    #Assert
    assert addition.get_result() == 9.0
