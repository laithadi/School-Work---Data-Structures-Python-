''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-16 
...................................................
'''

from functions import substitute

string = input("Input file: ")
fh_out = input("Output file: ")



string = open(string, "r")
fh_out = open(fh_out, "w")


string = string.read()
ciphertext = input("Enter ciphertext: ")

estring = substitute(string, ciphertext)

print(estring, file=fh_out)
print()
print("Done"