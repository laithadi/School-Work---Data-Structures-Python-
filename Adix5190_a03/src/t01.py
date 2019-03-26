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
from functions import stack_reverse
from utilities import array_to_stack

source = Stack()

l = input("Enter items (separate by space bar): ").split(" ")
array_to_stack(source, l)
#original stack inserted by user
print("Original:")
for i in source:
    print(i, end = " ")
print()
#the stack backwards 
print("Reverse:")   
stack_reverse(source)
for i in source:
    print(i, end = " ")