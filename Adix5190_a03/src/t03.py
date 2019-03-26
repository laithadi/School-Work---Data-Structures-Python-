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
from functions import stack_combine
from utilities import array_to_stack
#identify the sources as stacks
source1 = Stack()
source2 = Stack()
#grab stacks from user
l1 = input("Enter items (separate by space bar): ").split(" ")
l2 = input("Enter items (separate by space bar): ").split(" ")

array_to_stack(source1, l1)
array_to_stack(source2, l2)
#print source 1 
print("Source 1:")
for i in source1: 
    print(i, end = " ")
print()
#print source 2
print("Source 2:")
for i in source2:
    print(i, end = " ")
print()
#print the combined stack 
print("Combine:")   
target = stack_combine(source1, source2)
for i in target:
    print(i, end = " ")