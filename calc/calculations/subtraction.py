""" Subtraction Class """

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """ Subtraction class inheriting the base Calculation parent class """

    def get_result(self):
        """ Substract all numbers in the tuple """
        difference_value = 0.0
        for value in self.values:
            difference_value -= value
        return difference_value
