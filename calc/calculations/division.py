""" Division Class """

from calc.calculations.calculation import Calculation

class Division(Calculation):
    """ Division class inheriting the base Calculation parent class """

    def get_result(self):
        """ Divide all numbers in the tuple """
        quotient_value = 1.0
        for value in self.values:
            quotient_value = value / quotient_value
        return quotient_value
