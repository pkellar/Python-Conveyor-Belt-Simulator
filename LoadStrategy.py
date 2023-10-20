from math import trunc


# GRADING: BASIC_LOAD
def BasicLoad(loadMax):
    """
    Description: Generate basic load function and returns it

    param:  int - loadMax, max amount the station can fill at once
    return: load, function that the station will call to load units into its box
    """
    def load(self):
        """
        Description: Fill until full or station max

        param:  self instance of object that called the function
        return: void
        """
        box = self._box  # Get the station's box
        if box:
            boxMax = box.getUnitsLeft()
            # boxMax is how much can be added to the box, loadMax is station maximum
            if loadMax <= boxMax:
                box.addUnits(loadMax)
            else:
                box.addUnits(boxMax)

    return load


# GRADING: PERCENT_LOAD
def PercentLoad(percentMax):
    """
    Description: Generate percentage load function and returns it

    param:  int - percentMax, percentage of box that can be filled
    return: load, function that the station will call to load units into its box
    """
    def load(self):
        """
        Description: Fill until full or max percentage station allows

        param:  self instance of object that called the function
        return: void
        """
        box = self._box
        if box:
            calcMax = trunc(percentMax * box.getMaxLoad())
            boxMax = box.getUnitsLeft()
            # boxMax is how much can be added to the box, calcMax (calculated max) is the station maximum
            if calcMax <= boxMax:
                box.addUnits(calcMax)
            else:
                box.addUnits(boxMax)

    return load
