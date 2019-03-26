''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-24 
...................................................
'''

from Movie_utilities import genre_counts
from Movie_utilities import read_movies
fv = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fv)
count = genre_counts(movies)
print('Counts of number movies corresponding to each genre')
print(count)
fv.close()
