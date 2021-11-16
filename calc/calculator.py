""" Calculator Class """

from calc.history.calculations import Calculations

class Calculator:
    """ Calculator class contains methods to calculate """
    @staticmethod
    def get_last_result_value():
        """ Get the last result from Calculations class """
        return Calculations.get_last_calculation_result_value()
    @staticmethod
    def add_numbers(tuple_values: tuple):
        """ Add numbers in tuple together """
        Calculations.add_addition_calculation(tuple_values)
        return True
    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ Substract number in tuple """
        Calculations.add_subtraction_calculation(tuple_values)
        return True
    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ Multiply numbers in tuple """
        Calculations.add_multiplication_calculation(tuple_values)
        return True
    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ Divide numbers in tuple """
        Calculations.add_division_calculation(tuple_values)
        return True
