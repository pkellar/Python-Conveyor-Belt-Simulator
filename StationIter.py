from kellar_patrick.Station import Station


class StationIter:
    """
    Author: Patrick Kellar
    Description: Outside iterator for the conveyor just for stations
    """

    def __init__(self, system):
        self.__system = system

    # GRADING: ITER_STATION
    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        while self.__index != len(self.__system)-1:  # Iterate until end of the system
            self.__index += 1
            if isinstance(self.__system[self.__index], Station):  # Check if we are on a station
                return self.__system[self.__index]  # Return the next station
        else:
            raise StopIteration()
