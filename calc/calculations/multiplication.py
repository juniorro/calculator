""" Multiplication Class """

from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """ Multiplication class inheriting the base Calculation parent class """

    def get_result(self):
        """ Multiply all numbers in the tuple together """
        product_value = 1.0
        for value in self.values:
            product_value *= value
        return product_value
