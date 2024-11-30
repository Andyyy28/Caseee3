from abc import ABC, abstractmethod

# Abstract Base Class for Person
class Person(ABC):
    def __init__(self, name, email, contact_number, address):
        self.__name = name
        self.__email = email
        self._contact_number = contact_number
        self._address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @abstractmethod
    def display_info(self):
        pass
