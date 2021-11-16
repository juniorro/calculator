"""Calculation Class"""

class Calculation: #pylint: disable=too-few-public-methods
    """ Calculation abstract base class"""

    def __init__(self, values: tuple):
        """ constructor method """
        self.values = Calculation.convert_to_float(values)

    @classmethod
    def create(cls,values: tuple):
        """ Pass values to appropriate class """
        return cls(values)

    @staticmethod
    def convert_to_float(values):
        """ Convert values to floats and add into a tuple """
        float_values = []
        for value in values:
            float_values.append(float(value))
        return tuple(float_values)
