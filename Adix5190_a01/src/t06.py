''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-17 
...................................................
'''

import random

from functions import transpose

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

rows = len(a)
cols = len(a[0])

print("The matrix to transpose:")
for r in range(rows):
    for c in range(cols):
        print("{:<5d}".format(a[r][c]), end="")
    print()
print()

b = transpose(a)

row = len(b)
cols = len(b[0])

print('Transposed matrix:')

for r in range(rows):
    for c in range(cols):
        print('{:<5d}'.format(b[r][c]), end="")
    print()