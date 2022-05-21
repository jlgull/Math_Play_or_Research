#!/usr/bin/env python3

from time import perf_counter

choice = ''
again = 'Y'

while again == 'Y':
    
    length_counter = 0

    print('\n\nThis will print all the prime numbers in a range you supply.')

    start_number = int(input('\nPlease input starting number: '))
    end_number = int(input('Please input ending number  : '))

    continuous = input('\nContinuous output [Y] (good for speed testing) or pause every 20 lines [Enter]? ').upper()

    print(f'\nThe prime numbers from {start_number} to {end_number} are:\n')

    """
    The following code block sets a "proper" starting number.
    
    If starting number is less than 3, set it to 1. This is to keep any
    negative number from being generated by the next algorithm.
    
    The next algorithm makes certain that the starting number is odd by:
    
    First: subtract the remainder of the starting number divided by 3 from
    itself. For example (the first number is the one entered by the user):
    100 - (the remainder of 100 / 3, which is 1) = 99   (OK!)
    101 - (the remainder of 100 / 3, which is 2) = 98   (NOT OK)
    102 - (the remainder of 100 / 3, which is 0) = 102  (NOT OK)
    
    Then, if needed: we need an odd starting number. Check to see if it is
    even. If it is, we add 1 to it to make it odd. For example:
    101 - (the remainder of 100 / 3, which is 2) = 98 + 1 = 99   (OK!)
    102 - (the remainder of 100 / 3, which is 0) = 102 + 1 = 103 (OK!)
    """

    if start_number < 3:
        start_number = 1
    else:
        start_number = start_number - (start_number % 3)
        if start_number % 2 == 0:
            start_number = start_number + 1

    # get the time, to determine how quickly it runs
    time1 = perf_counter()

    """
    These two loops do the heavy lifting.

    The outside loop (i) loops from the starting number to the ending number
    stepping by 2. This is the number being checked to see if it prime or not.

    It is _assumed_ that the number being checked is prime (prime_num = 1).

    The inside loop (j) loops from 3 to the square root of i, plus 1 - stepping by 2.
    This loop does not go until i+1. There's no reason to go until j equals i.

    Check to see if i is evenly divisible by j. If so, then the number being checked
    (i) is _not_ prime and prime_number is set to 0 and the inside loop is stopped.
    """

    for i in range(start_number, end_number + 1, 2):

        prime_num = 1

        for j in range(3, int(i ** 0.5) + 1, 2):

            if i % j == 0:
                prime_num = 0
                break

        # Check to see if prime_num is still 1, meaning a prime was found. If it is,
        # print it out in columns of 15, padded with 5 spaces. Pause every 20 lines -
        # if the continuous variable is not set to Y
        if prime_num == 1:
            length_counter += 1
            print(f'{i:5}', end=' ' if length_counter % 15 != 0 else '\n')

            if length_counter % 300 == 0 and continuous != 'Y':
                choice = input('\nPaused... press Enter to continue or Z to quit...\n').upper()

                if choice == 'Z':
                    break

    # get the time again, then print the difference between time2 and time1
    time2 = perf_counter()
    print(f'\n\nTime to execute = {time2 - time1:.05f} seconds.')

    again = input('\nRun again? [Y for Yes, Enter for no]: ').upper()

print('\nBye! Thanks for using my program!')
