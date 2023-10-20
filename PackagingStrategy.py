# GRADING: BASIC_PACKAGE
def BasicPackage(boxCount):
    """
    Description: Generate basic packaging function and its output and returns it

    param:  int - boxCount, how many boxes needed to make a package
    return: package, packageOut, functions that the station will call to package the box and output its current
        packaging state
    """
    packagesComplete = 0
    waiting = []

    def package(self):
        """
        Description: Will move box along or put it into a package if full

        param:  self instance of object that called the function
        return: void
        """
        nonlocal packagesComplete
        nonlocal waiting
        box = self._box
        if box:
            if box.getUnitsLeft() == 0:  # Check if the box is full
                waiting.append(box)  # If so, add to waiting array
                self.removeBox()    # Remove the box from the station
                if len(waiting) == boxCount:   # Checks if a package is full
                    packagesComplete += 1  # Increments packages complete
                    waiting = []    # Clears waiting

    def packageOut():
        """
        Description: Output the current basic packaging information of the station

        return: void
        """
        nonlocal packagesComplete
        nonlocal waiting
        idList = ""

        # Builds ID list of the boxes waiting
        for index, box in enumerate(waiting):
            if index+1 == len(waiting):  # Since we don't want a comma at the end
                idList += str(box.getID())
            else:
                idList += str(box.getID()) + ", "

        print("Packages every", boxCount, "boxes")
        print("Currently has unpackaged box ids:", idList)
        print("Packages Complete:", packagesComplete)

    return package, packageOut


# GRADING: RESTRICTED_PACKAGE
def RestrictedPackage(boxCount, minimum, maximum):
    """
    Description: Generate basic packaging function and its output and returns it

    param:  int - boxCount, how many boxes needed to make a package
    param:  int - minimum, lower range of units allowed
    param:  int - maximum, upper range of units allowed
    return: package, packageOut, functions that the station will call to package the box and output its current
        packaging state
    """
    packagesComplete = 0
    waiting = []

    def package(self):
        """
        Description: Will move box along or put it into a package if in range of min and max

        param:  self instance of object that called the function
        return: void
        """
        nonlocal packagesComplete
        nonlocal waiting
        box = self._box
        if box:
            if minimum <= (box.getMaxLoad() - box.getUnitsLeft()) <= maximum:  # Check if the box is in range
                waiting.append(box)  # If so, add to waiting array
                self.removeBox()    # Remove the box from the station
                if len(waiting) == boxCount:   # Checks if a package is full
                    packagesComplete += 1  # Increments packages complete
                    waiting = []    # Clears waiting

    def packageOut():
        """
        Description: Output the current restricted packaging information of the station

        return: void
        """
        nonlocal packagesComplete
        nonlocal waiting
        idList = ""

        # Builds ID list of the boxes waiting
        for index, box in enumerate(waiting):
            if index+1 == len(waiting):  # Since we don't want a comma at the end
                idList += str(box.getID())
            else:
                idList += str(box.getID()) + ", "

        print("Size range [" + str(minimum) + ", " + str(maximum) + "]")
        print("Packages every", boxCount, "boxes")
        print("Currently has unpackaged box ids:", idList)
        print("Packages Complete:", packagesComplete)

    return package, packageOut
