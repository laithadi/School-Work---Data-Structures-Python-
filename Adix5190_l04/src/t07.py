''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-11 
...................................................
'''

from utilities import list_test
fh = open("movies.txt", "r")
a = fh.readlines() 
list_test(a)
fh.close()