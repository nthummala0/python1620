class Person:
    """
    A class representing details for a person object.
    """
    def __init__(self, name, age=0):
        """
        Method to set default values of person object.
        :param name: Person's full name.
        :param age: Person's age.
        """
        self.__name = name
        self.__age = age

    def get_name(self):
        """
        Method to access person's name.
        :return: Person's full name.
        """
        return self.__name

    def set_name(self, name):
        """
        Method to modify a person's name.
        :param name: New name.
        """
        self.__name = name

# Example Usage
p1 = Person('Jane')  # Name = Jane Age = 6
p2 = Person('John', 10)  # Name = John Age = 10
