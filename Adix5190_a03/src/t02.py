''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-31 
...................................................
'''


from Stack_array import Stack
from utilities import array_to_stack
#grab the stack from user 
source = Stack()
l = input("Enter items (separate by space bar): ").split(" ")
array_to_stack(source, l)
#print the orginal 
print("Original:")
for i in source:
    print(i, end = " ")
print()
#print the reverse stack 
print("Reverse:")   
source.reverse()
for i in source:
    print(i, end = " ")