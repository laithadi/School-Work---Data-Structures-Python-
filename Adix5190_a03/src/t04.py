''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-01 
...................................................
'''

from Stack_array import Stack
from utilities import array_to_stack
#identifting the sources and target as stacks 
target = Stack()
source1 = Stack()
source2 = Stack()
#grabing the sources from user
l1 = input("Enter items (seperated by space bar): ").split(" ")
l2 = input("Enter items (seperated by space bar): ").split(" ")

array_to_stack(source1, l1)
array_to_stack(source2, l2)
#print the resulting stack 
print("Combine:")   
target.combine(source1, source2)
for i in target:
    print(i, end = " ")