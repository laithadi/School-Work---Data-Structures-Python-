''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-21 
...................................................
'''



from Movie_utilities import get_by_year
from Movie_utilities import read_movies

fv = open("movies.txt", "r")
year = int(input('Enter year: '))
movies = read_movies(fv)


ymovies = get_by_year(movies, year)


print(ymovies)
