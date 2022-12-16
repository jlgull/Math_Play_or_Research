#!/usr/bin/python3
#
# Author - Jonathan Heard
#
# Given String
text = 'KBDNM-R8CD9-RK366-WFM3X-C7GXK'
# splitting the string using - as a separator
res = text.split('-')
# length of split string list
x = len(res)

print(f'\nThe raw key is {text}\n')

print(f'The partitioned key is {res}\n')

print(f'The number of key segments is {x}.\n')

# Define empty dictionary

keys = []

# Extract the keys and append them to the dictionary

for i in range(1, len(res)+1):
    keys.append('key_segment ' + str(i))

data = dict(zip(keys, res))

for keys, items in data.items():
    print(keys, " = ", items)