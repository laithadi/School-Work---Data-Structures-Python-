''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-10 
...................................................
'''

from Priority_Queue_array import Priority_Queue

pq = Priority_Queue() 
pq.insert(1)
pq.insert(2)
pq.insert(3)
pq.insert(4)

print(pq._values)

key = 2
print(key)

target1, target2 = pq.split_key(key)

print(target1._values, target2._values)