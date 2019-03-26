''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-22 
...................................................
'''

from Movie_utilities import get_by_rating
from Movie_utilities import read_movies

fv = open("movies.txt", "r")
movies = read_movies(fv)

rating = float(input('Enter a rating here: ')) 

rmovies = get_by_rating(movies, rating)

print(rmovies)





    



