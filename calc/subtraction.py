"""Subtraction inheriting value A and value B from the calculation class"""
#Namespace: similar to files and folders, classes are files and the folders organize the classes
#It is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Subtraction(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def get_result(self):
        """ Encapsulation: uses self to reference data in the instance of the object """
        return self.value_a - self.value_b
