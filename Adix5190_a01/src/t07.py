''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-18 
...................................................
'''

import random

from functions import rotate_right

r = int(input('Number of rows: '))
c = int(input('Number of columns: '))
a = []

print()

for i in range(0, r):
    a1 = []
    for i in range(0, c):
        rand = random.randint(-10, 10)
        a1.append(rand)
    a.append(a1)

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

rows = len(a)
cols = len(a[0])

print("The matrix to rotate:")
for r in range(rows):
    for c in range(cols):
        print("{:<5d}".format(a[r][c]), end="")
    print()
print()

ra = rotate_right(a)

row = len(ra)
cols = len(ra[0])

print('Rotated matrix:')

for r in range(rows):
    for c in range(cols):
        print('{:<5d}'.format(ra[r][c]), end="")
    print()
