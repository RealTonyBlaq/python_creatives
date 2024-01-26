#!/usr/bin/python3

" Module for Coal City Estate "


class CC_Estate:
    """ Defines the class CC_Estate """

    def __init__(self, state, lga, country="Nigeria"):
        """ Initializes the attributes """
        self.__state = state
        self.__lga = lga
        self.__country = country

    def string_validator(self, value):
        """ Validates a string """
        if not isinstance(value, str):
            raise TypeError("{} must be a string".format(value))
        if value is None or value == "":
            raise ValueError("{} cannot be empty".format(value))

    def integer_validator(self, value):
        """ Validates an integer """
        if not isinstance(value, int):
            raise TypeError("{} must be a number".format(value))
        if value <= 0 or value is None:
            raise ValueError("{} must be >= 1".format(value))


class House(CC_Estate):
    """
    This class is for an estate with:

    Class Attributes:
    -----------------

    h_number: Private class attribute house number which
            increases with every instance creation
    """
    __h_number = 0

    def __init__(self, name=None, house_type=None, occupants=1):
        """
        Initializes the attributes

        Parameters:
        -----------

        name: Name of house owner
        type: Type of the house which could be:
            bungalow, one-story, detached duplex, etc.
        occupants: Number of occupants in the house
        hn: House number, will be set to h_number
        """
        House.__h_number += 1
        self.string_validator(name)
        self.__name = name
        self.string_validator(house_type)
        self.__house_type = house_type
        self.integer_validator(occupants)
        self.__occupants = occupants
        self.__hn = House.__h_number

    @property
    def name(self):
        """ Returns the value for name """
        return self.__name

    @name.setter
    def name(self, value):
        """ Sets name to value """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "" or value is None:
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def house_type(self):
        """ Returns the value of h_type """
        return self.__house_type

    @house_type.setter
    def house_type(self, value):
        """ Sets house_type to value """
        if not isinstance(value, str):
            raise TypeError("House type must be a string")
        if value == "" or value is None:
            print("House type has been set to Bungalow")
            self.__house_type = "Bungalow"
        else:
            self.__house_type = value

    @property
    def occupants(self):
        """ Returns the number of occupants """
        return self.__occupants

    @occupants.setter
    def occupants(self, value):
        """ Sets occupants to value """
        if not isinstance(value, int):
            raise TypeError("Number of occupants must be an integer")
        if value <= 0 or value is None:
            raise ValueError("Number of occupants must be >= 1")
        self.__occupants = value

    def __repr__(self):
        """ Returns a string representation of CC_Estate """
        return "CC_Estate({}, {}, {})"\
            .format(self.__name, self.__house_type, self.__occupants)

    def __str__(self):
        """ Returns a string a story of the house details """
        return "House #{} is a {} with {} occupants. It is owned by {}"\
            .format(self.__hn, self.__house_type,
                    self.__occupants, self.__name)
