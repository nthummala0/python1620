class Person:
    """
    A class representing details for a person object.
    """
    def __init__(self, name: str, age=0) -> None:
        """
        Method to set default values of person object.
        :param name: Person's full name.
        :param age: Person's age.
        """
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        """
        Method to access person's name.
        :return: Person's full name.
        """
        return self.__name

    def set_name(self, name: str) -> None:
        """
        Method to modify a person's name.
        :param name: New name.
        """
        self.__name = name
