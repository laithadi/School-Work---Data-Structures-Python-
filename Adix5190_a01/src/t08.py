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

from functions import clean_list

values = []

for i in range(0, 25):
    rand_int = random.randint(0, 5)
    values.append(rand_int)
    
print('Values:', values)

clean_list(values)