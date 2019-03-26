''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-24 
...................................................
'''

from Movie_utilities import get_by_genres
from Movie_utilities import read_movies 
from Movie_utilities import read_genres

fv = open("movies.txt", "r")
movies = read_movies(fv)

genres = read_genres()

gmovies = get_by_genres(movies, genres)

print(gmovies)
    
    

