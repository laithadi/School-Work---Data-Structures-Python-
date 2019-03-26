''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-10 
...................................................
'''

from functions import pq_split_key
from Priority_Queue_array import Priority_Queue
source = Priority_Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
print(source._values)
key = 2
print(key)
target1, target2 = pq_split_key(source, key)

print(target1._values, target2._values)
