"""
Program Name: Python, Iterator Pattern, Strategy Pattern
Author: Patrick Kellar
Class: CSC-461-M01 Fall 2022
Description: This is a conveyer belt simulator using the iterator and strategy patterns.
Last tier passed: 9


Grading tags in for all lines marked with *		_X_

Tierless str meets D in SOLID (hidden test)*		_X_
Check if done, but not all tiers are passing		___

1. Initial Show system\Got it compiling
Menu\initial system working                     _X_
Bad input handled								_X_

2. Add Default Box
Added and shown properly						_X_
Second+ box ignored								_X_

3. Basic Update
Moves along belts								_X_
Moves to next station\belt						_X_
Drops off the end when reached					_X_
String format correct							_X_
Iterator used*									_X_

4. Multi Update
Updates correct amount							_X_
Bad input handled								_X_
String format correct							_X_

5. Show station details (default)
Shows stations details properly 				_X_
Iterator used*									_X_
6. Add box
Added and shown properly						_X_
Second+ box ignored								_X_
Bad input handled								_X_

7. Tester Conveyer part 1
Initial system and station details correct 		_X_
A single box still able to be added				_X_
Update with one default box works				_X_
Loading works 									_X_
Formatting correct 								_X_

8. Tester Conveyer part 2
Packaging works 								_X_
Formatting correct 								_X_
Strategy pattern for loading*					_X_
Strategy pattern for packaging*					_X_


9. Custom belt **
String formatting correct						_X_
Everything still works 							_X_
Bad input handled 								_X_


** This tier has 3 tests associated with it. 9A tests all belt/station orderings. 9B tests all combinations of
packaging and fill. 9C tests error checking.

"""
from kellar_patrick.Belt import Belt
from kellar_patrick.Box import Box
from kellar_patrick.Conveyer import Conveyer
from kellar_patrick.Station import Station


def cleanInput(prompt):
    result = input(prompt)
    # Strips out blank lines in input
    while result == '':
        result = input()

    return result


def main():
    """
    Description: Main menu of the conveyor simulator
    return: void
    """

    def dCheck():
        """
        Description: This function is the -1 SOLID D check
        return: void
        """
        # Make a box and a belt
        box1 = Box()
        belt = Belt()
        # Add box to belt
        belt.addBox(box1)

        # Make a box and station
        box2 = Box()
        station = Station()
        # Add box to the station
        station.addBox(box2)

        # Add default box to the system
        system.addBox()

        # GRADING: TO_STR
        print(box1, end="")
        print(box2, end="")
        print(belt)
        print(station)
        print(system)

    # Make a conveyer
    system = Conveyer()
    menu = "\n" \
           "1) Add Default Box\n" \
           "2) Move Belt One Time Unit\n" \
           "3) Move Belt X Time Units\n" \
           "4) Show Station Details\n" \
           "5) Add Box\n" \
           "6) Make Tester Conveyer Belt\n" \
           "7) Make New Conveyer Belt\n" \
           "0) Quit\n"

    choice = -1

    print(system)
    while choice != 0:
        try:
            print(menu)
            choice = int(cleanInput("Choice:> "))

            # add default box
            if choice == 1:
                system.addBox()
                print(system)

            # update one time
            elif choice == 2:
                system.moveBelt()

            # update X number of times
            elif choice == 3:
                updates = int(cleanInput("How many updates:> "))
                system.moveBelt(updates)

            # print out station details
            elif choice == 4:
                # GRADING: LOOP_STATION
                system.iterateStations()

            # make a new box of any size
            elif choice == 5:
                maxUnits = int(cleanInput("How many units:> "))
                if maxUnits < 1:
                    print("Please, input a positive integer")
                else:
                    system.addBox(maxUnits)
                    print(system)

            # make new system
            elif choice == 6:
                system.setTestConveyer()
                print(system)

            # make new system
            elif choice == 7:
                system.newConveyer()
                print(system)

            # debug/check for D in SOLID in __str__
            elif choice == -1:
                dCheck()

            elif choice == 0:
                choice = 0
            else:
                print("Input an option in the range 0-7")
        except ValueError:
            print("Please, input a positive integer")


if __name__ == '__main__':
    main()
