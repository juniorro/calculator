""" Addition Class """

from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ Addition class inheriting the base Calculation parent class """

    def get_result(self):
        """ Add all numbers in the tuple together """
        sum_value = 0.0
        for value in self.values:
            sum_value += value
        return sum_value
