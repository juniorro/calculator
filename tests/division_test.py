""" Testing Division """
from calc.calculations.division import Division

def test_calculation_division():
    """ Testing static method for division """
    #Arrange
    mynumbers = (10.0, 5.0)
    #Act
    division = Division(mynumbers)
    #Assert
    assert division.get_result() == 0.5
