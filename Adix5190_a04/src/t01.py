''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-10 
...................................................
'''
from Queue_array import Queue
from functions import queue_is_identical
source1 = Queue()
source2 = Queue()
source1.insert(11)
source1.insert(21)
source1.insert(31)
source2.insert(11)
source2.insert(21)
source2.insert(31)
print(source1._values)
print(source2._values)
identical = queue_is_identical(source1, source2)

print(identical)



