''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-01 
...................................................
'''

from functions import is_palindrome_stack

string = input("String: ")

if is_palindrome_stack(string) == True:
    print("{} is a palindrome.".format(string))
else:
    print("{} is not a palindrome.".format(string))