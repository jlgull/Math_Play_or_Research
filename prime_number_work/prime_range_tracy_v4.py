#!/usr/bin/env python3

from time import perf_counter

again = 'Y'

while again == 'Y':
    choice = ''
    end_number = 0
    primes_found = 0
    i = 0

    print('\n\nThis will print all the prime numbers in a range you supply.')

    start_number = int(input('\nPlease input an odd starting number - 3 or greater (as 2 is prime): '))

    # Checking to see if the rules are followed. If start_number is less than 3, make it 3.
    # If start_number is even, make it odd by subtracting 1. Let the user know if it was changed.
    if start_number < 3 or start_number % 2 == 0:
        if start_number < 3:
            start_number = 3
        else:
            start_number = start_number - 1
        print(f'\n> Changing starting number to {start_number}. <\n')

    # Enforce the rule that the end_number must be greater than the start_number.
    while end_number <= start_number:
        end_number = int(input(f'Please input ending number (greater than {start_number}): '))

    continuous = input('\nContinuous output [Y] (good for speed testing) or pause every 20 lines [Enter]? ').upper()

    print(f'\nThe prime numbers from {start_number} to {end_number} are:\n')

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
            primes_found += 1
            print(f'{i:5}', end=' ' if primes_found % 15 != 0 else '\n')

            if primes_found % 300 == 0 and continuous != 'Y':
                choice = input('\nPaused... press Enter to continue or Z to abort...\n').upper()

                if choice == 'Z':
                    break

    # get the time again, print the time difference between time2 and time1, print the number
    # of primes found between the starting number and the ending number (or, if the program was
    # aborted, the last number processed), and print the percentage of primes found in a range.
    time2 = perf_counter()
    ending_number = end_number if choice != 'Z' else i
    print(
        f'\n\nIn {time2 - time1:.5f} seconds, {primes_found} prime numbers were found between {start_number} '
        f'and {ending_number}.')
    print(
        f'\nPercentage of prime numbers found in the range: '
        f'{(primes_found / (ending_number - start_number)) * 100:.2f}%')

    again = input('\n\nRun again? [Y for Yes, Enter for no]: ').upper()

    print('\nBye! Thanks for using my program!')
