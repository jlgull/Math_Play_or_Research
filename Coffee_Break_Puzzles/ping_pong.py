#!/usr/bin/python3
#
# Author: Jonathan Heard
# Work on calculating prime numbers and also timing them to the second.
#   To time to nSeconds, switch which of the perf_counter items to use,
#   and also change the format and label in the print statmets.
#

#
# Import all required items.
#
from kennedy_13 import clear, get_data
""" This is a module written to contain tools used throughout the main program
        to reduce the duplication of code as the designed moved forward.
        clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
                    independent or agnostic.
        get_data    - Is used for all data entry requests. It used try/except to ensure that the data
                        entered is the type expected and it also expects a clarifying question or statement. 
"""

from time import perf_counter, perf_counter_ns

#
# End of the Import section.
#


#
# Define functions
#


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    letters = ['a', 'b', 'c', 'd']
    print(len(letters[1:-1]))



    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run this again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of Program
