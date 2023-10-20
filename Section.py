class Section:
    """
    Author: Patrick Kellar
    Description: Controls and holds the box and symbols that make up a section
    """

    def __init__(self, symbols):
        """
        Description: Section constructor

        param:  self
        param:  symbols    String representing the section
        return: a section object
        """
        self._box = None
        self.__symbols = symbols

    def addBox(self, box):
        """
        Description: Adds a box to the section

        param:  self
        param:  box() object to be added
        return: void
        """
        # Only add a box if there is already one there
        if not self.hasBox():
            self._box = box

    def removeBox(self):
        """
        Description: Removes the box from the section

        param:  self
        return: void
        """
        self._box = None

    def hasBox(self):
        """
        Description: Returns true if section has a box, false if not

        param:  self
        return: True or False
        """
        if self._box is None:
            return False
        else:
            return True

    def __str__(self):
        """
        Description: Returns string version of the section

        param:  self
        return: String of section
        """
        if self.hasBox():  # Add box string if we have one
            return self._box.__str__() + self.__symbols
        else:
            return '\n' + '\n' + self.__symbols

    def move(self, previous):  # NOTE: this is previous from the perspective of iterating backwards
        """
        Description: Removes box from this section and moves it to the one in front of it

        param:  self
        param:  previous    Section object that is in front of this one
        return: void
        """
        if self.hasBox():  # Checks if this section has a box
            if previous is not None:  # Make sure to not add a box to a section that doesn't exist
                previous.addBox(self._box)  # Add mox to previous section
            self.removeBox()  # Remove box from this section


