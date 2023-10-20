from kellar_patrick import LoadStrategy, PackagingStrategy
from kellar_patrick.Belt import Belt
from kellar_patrick.Box import Box
from kellar_patrick.Station import Station
from kellar_patrick.StationIter import StationIter


def loadInput(prompt, maxInput=0):
    """
    Description: Gets user input with prompt in the maxInput range

    param:  prompt      String to be output
    param:  maxInput    int - The Highest number that can be added
    return: result      The input integer
    """
    result = input(prompt)
    # Strips out blank lines in input
    while result == '':
        result = input()

    result = int(result)
    # Checks if range needs to be checked
    if maxInput != 0:
        if not 1 <= result <= maxInput:
            raise ValueError

    return result


def cleanInput(prompt, maxInput=0):
    """
    Description: Gets user input with prompt in the maxInput range

    param:  prompt      String to be output
    param:  maxInput    int - The Highest number that can be added
    return: result      The input integer
    """
    result = input(prompt)
    # Strips out blank lines in input
    while result == '':
        result = input()
    # Checks if range needs to be checked
    if maxInput != 0:
        if not 1 <= int(result) <= int(maxInput):
            print("Input an option in the range 1-" + str(maxInput))
            raise TypeError

    return result


class Conveyer:
    """
    Author: Patrick Kellar
    Description: Controls and holds the conveyor
    """

    def __init__(self):
        # Sets the default conveyer initially
        self.__conveyer = [Belt(), Belt(), Station(), Belt(), Belt(), Station()]

    # GRADING: ITER_ALL
    def __iter__(self):
        """
        Description: Walking through the collection backwards returning one at a time and update the location

        param:  self
        return: self
        """
        self.__index = len(self.__conveyer)
        # Similar to an interface
        return self

    def __next__(self):
        """
        Description: Controls the iterator

        param:  self
        return: the next section in the conveyer array
        """
        if self.__index == 0:
            raise StopIteration()
        self.__index -= 1  # Equivalent to next()
        return self.__conveyer[self.__index]  # Equivalent to get()

    def addBox(self, maxLoad=10, units=0):
        """
        Description: Adds a box to the front section

        param:  maxLoad     int - Max units the box can have
        param:  units       int - amount of space filled in a box
        return: void
        """
        self.__conveyer[0].addBox(Box(maxLoad, units))

    def moveBelt(self, moves=1):
        """
        Description:  Moves the boxes on each section to the right x amount of times

        param:  moves     int - How many times to move the boxes right
        return: void
        """
        #
        for _ in range(moves):
            # Packages each station
            for i in self.getStationIter():
                i.package()

            # Moves the box in each section
            previous = None
            # GRADING: LOOP_ALL
            for section in self:
                section.move(previous)
                # Save previous to know it is safe to move box there
                previous = section

            # Loads each station
            for station in self.getStationIter():
                station.load()
            print(self)

    def __str__(self):
        """
        Description:  String version of a conveyer

        param:  self
        return: ids + units + symbols - appended strings representing the conveyer
        """
        # newline at start since I flip the strings at the end
        ids = "\n"
        units = "\n"
        symbols = ""
        # Iterate through self
        for section in self:
            # Get the section's string
            tempStr = section.__str__()
            # Split it on newlines
            tempStr = tempStr.splitlines()

            # Just append spaces if there is no box
            if tempStr[0] == "":
                ids += "    "
                units += "    "
            else:  # Flip the ids and units (since I'm iterating backwards) and give them the right spacing
                ids += tempStr[0].ljust(4, ' ')[::-1]
                units += tempStr[1].ljust(4, ' ')[::-1]
            # Symbols individually the same forwards as backwards
            symbols += tempStr[2]

        # Flip each chunk, append together to be output
        return ids[::-1] + units[::-1] + symbols[::-1]

    def getStationIter(self):
        """
        Description:  Gets an iterator that returns stations in order

        param:  self
        return: StationIter()
        """
        return StationIter(self.__conveyer)

    def setTestConveyer(self):
        """
        Description:  Sets a conveyor with a test pattern that uses belts and stations with each type of packaging
                        and loading strategies
        param:  self
        return: void
        """

        # Clear current conveyer
        self.__conveyer = []

        self.__conveyer.append(Belt())
        self.__conveyer.append(Station())
        self.__conveyer.append(Belt())
        self.__conveyer.append(Belt())

        # Get basic packing behavior function and its output function with a boxCount of 2
        packageBehavior, packageOut = PackagingStrategy.BasicPackage(2)
        # Make a new station with basic loading and packaging
        station = Station(LoadStrategy.BasicLoad(2), packageBehavior, packageOut)
        self.__conveyer.append(station)  # Add the new station to the conveyer
        self.__conveyer.append(Belt())
        self.__conveyer.append(Belt())

        # Get Restricted packing behavior function and its output function with a boxCount of 2,
        #   min of 0, and max of 100
        packageBehavior, packageOut = PackagingStrategy.RestrictedPackage(3, 0, 1000)
        # Make a new station with percent load and restricted packaging
        station = Station(LoadStrategy.PercentLoad(0.5), packageBehavior, packageOut)
        self.__conveyer.append(station)  # Add the new station

    def iterateStations(self):
        """
        Description:  Output the information of each station

        param:  self
        return: void
        """
        stationNum = 0
        for i in self.getStationIter():
            stationNum += 1
            print("\nStation " + str(stationNum))
            print("Has box: " + str(i.hasBox()))
            # have the section call its package output function
            i.outputPackage()

    def newConveyer(self):
        """
        Description:  Lets a user make their own conveyer

        param:  self
        return: void
        """
        self.__conveyer = []  # Clear the conveyer
        another = 'y'

        while another != 'n':
            try:  # Add a belt or station
                sectionType = int(cleanInput("Belt (1) or Station (2):> ", 2))
                if sectionType == 1:  # Add a belt
                    length = int(cleanInput("Length:> "))  # How many belts to add
                    for count in range(length):
                        self.__conveyer.append(Belt())
                elif sectionType == 2:  # Add a station
                    # Pick load behavior
                    loadBehavior = loadInput("Load behavior: None (1), Basic (2), or Percentage (3):> ", 3)
                    loadStrategy = None
                    if loadBehavior == 2:  # Basic load behavior
                        numUnits = int(cleanInput("Number of units:> "))  # Max load units
                        loadStrategy = LoadStrategy.BasicLoad(numUnits)
                    elif loadBehavior == 3:  # Percentage load behavior
                        percentage = float(cleanInput("Percentage of box:> "))  # Max percentage
                        if percentage.is_integer():  # Checks if user entered an integer
                            percentage = percentage/100  # Turns int into a float
                        loadStrategy = LoadStrategy.PercentLoad(percentage)

                    packageStrategy, packageOut = None, None
                    # Pick packaging behavior
                    packageBehavior = int(cleanInput("Packaging behavior: None (1), Basic (2), or Restricted (3):> "))
                    if packageBehavior == 2:  # Basic packaging behavior
                        numBoxes = int(cleanInput("Number of boxes per package:> "))
                        packageStrategy, packageOut = PackagingStrategy.BasicPackage(numBoxes)
                    elif packageBehavior == 3:  # Restricted packaging behavior
                        numBoxes = int(cleanInput("Number of boxes per package:> "))
                        minimum = int(cleanInput("Minimum units:> "))
                        maximum = int(cleanInput("Maximum units:> "))
                        packageStrategy, packageOut = PackagingStrategy.RestrictedPackage(numBoxes, minimum, maximum)
                    self.__conveyer.append(Station(loadStrategy, packageStrategy, packageOut))
                another = cleanInput("Add another component (n to stop):> ")
            except TypeError:
                another = cleanInput("Add another component (n to stop):> ")
            except ValueError:
                print("Cannot accept value")
                another = cleanInput("Add another component (n to stop):> ")
