''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-18 
...................................................
'''
from functions import shift

string = input("Input file: ")
fh_out = input("Output file: ")
string = open(string, "r")
fh_out = open(fh_out, "w")
string = string.read()
n = int(input("Enter shift: "))
estring = shift(string, n)
print(estring, file=fh_out)
print()
print("Done")




