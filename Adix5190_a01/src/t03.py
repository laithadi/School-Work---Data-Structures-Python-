''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-18 
...................................................
'''

from functions import is_palindrome
    
s = input('Enter a palindrome: ')

s = s.lower()

palindrome = is_palindrome(s)

print(palindrome)