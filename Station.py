from kellar_patrick.Section import Section


class Station(Section):
    """
    Author: Patrick Kellar
    Description: Controls and holds strategies of the station
    """

    def __init__(self, loadBehavior=None, packagingBehavior=None, packageOut=None):
        """
        Description: Constructs a station object

        param:  self
        param:  loadBehavior    -   function that will load the box in the station
        param:  packagingBehavior    -   function that will package the box in the station
        param:  packageOut    -   function that will output the packaging info of the station
        return: station object
        """
        self.__loadBehavior = loadBehavior
        self.__packagingBehavior = packagingBehavior
        self.__packageOut = packageOut
        super().__init__("XXXX")  # Symbols to represent a station

    def load(self):
        """
        Description: Runs the loading function

        param:  self
        return: void
        """
        if self.__loadBehavior is not None:
            self.__loadBehavior(self)

    def package(self):
        """
        Description: Runs the packaging function

        param:  self
        return: void
        """
        if self.__packagingBehavior is not None:
            self.__packagingBehavior(self)

    def outputPackage(self):
        """
        Description: Runs the packaging output function

        param:  self
        return: void
        """
        if self.__packageOut is not None:
            self.__packageOut()
        else:
            print("Packaging: None")

