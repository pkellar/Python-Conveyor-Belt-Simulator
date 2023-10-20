def genID():
    """
    Description: Generates box ids

    return: number of next box id
    """
    curr = 1
    while True:
        yield curr
        curr += 1


class Box:
    """
    Author: Patrick Kellar
    Description: Controls and holds the box with id, maxLoad, and units
    """
    # Call ID generator function
    idGen = genID()

    def __init__(self, maxLoad=10, units=0):
        """
        Description: Constructs a box object

        param:  self
        param:  maxLoad     int - total amount of units that can fit in the box
        param:  units       int - how many units are in the box
        return: box object
        """
        self.__id = next(self.idGen)
        self.__maxLoad = maxLoad
        self.__units = units

    def __str__(self):
        """
        Description: Returns string version of box

        param:  self
        return: string of box
        """
        return str(self.__id) + "\n" + str(self.__units) + "\n"

    def getMaxLoad(self):
        return self.__maxLoad

    def getUnitsLeft(self):  # Returns amount of space left in the box
        return self.__maxLoad - self.__units

    def addUnits(self, newUnits):
        self.__units += newUnits

    def getID(self):
        return self.__id
