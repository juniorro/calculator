"""This is our calculation base class / Abstract Class"""
class Calculation:  # pylint: disable=too-few-public-methods
    """This is our calculation base class / Abstract Class"""
    #contstructor and it is the first function called when an object of the class is instantiated
    def __init__(self,value_a, value_b):
        #self references the instantiated object of the class
        #Istance properties  being shared with child classes (addition, subtraction, etc...)
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """ Class Factory Method <- bound to the class and not the instance of the class """
        return cls(value_a,value_b)
