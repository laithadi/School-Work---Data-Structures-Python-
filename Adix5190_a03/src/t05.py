''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-01 
...................................................
'''

from functions import has_balanced_brackets

BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3

string = input("Enter a string: ")
balanced = has_balanced_brackets(string)

if balanced == MORE_LEFT:
    print("'{}' has more left brackets.".format(string))
elif balanced == BALANCED:
    print("'{}' has balanced brackets.".format(string))
elif balanced == MORE_RIGHT:
    print("'{}' has more right brackets.".format(string))
else:
    print("'{}' has mismatched brackets.".format(string))
    
    