''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-01 
...................................................
'''

from functions import postfix

string = input("Enter a string: ")
answer = postfix(string)

print("{} evaluates to {}".format(string, answer))


#not too sure how to fix the error, i believe its something with the stack being empty but i cant think of a way to resolve it on time
