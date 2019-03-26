''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-22 
...................................................
'''
    
    
from Movie_utilities import get_by_genre
from Movie_utilities import read_movies
fv = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fv)
genre = int(input('Enter a genre to search for: '))
gmovies = get_by_genre(movies, genre)
print(gmovies)


