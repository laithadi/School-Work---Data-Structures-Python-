"""
-------------------------------------------------------
Movie class definition.
-------------------------------------------------------
Author:  Laith Adi
ID:      170265190
Email:   adix5190@mylaurier.ca
Section: CP164 
__updated__ = "2019-01-08"
-------------------------------------------------------
"""

from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    title = input('Title: ')
    yr_of_release = input('Year of release: ')
    director = input('Director: ')
    rating = input('Rating: ')
    genres = read_genres()
    menu() 
    
    movie = Movie(title, yr_of_release, director, rating, genres)
    
    

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    genres = []
    line = line.split('|')
    title = line[0]
    year = int(line[1])
    director = line[2]
    rating = float(line[3])
    x = line[4].split(',')
    for i in x:
        i = int(i)
        genres.append(i)
    movie = Movie(title, year, director, rating, genres)
        
    return movie




def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    movies = []
    fv.seek(0)
    
    for line in fv:
        movies.append(read_movie(line))
        
    return movies




def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Returns:
        None
    -------------------------------------------------------
    """

    print ('Genres')
    #counter
    x = 0 
    #as long as we moving up the list UNTIL we reach the length of the constant list 
    while x != len(Movie.GENRES):
        #print the number and name of genre 
        print ('{}: {}'.format(x, Movie.GENRES[x]))
        #add one every time it runs
        x+=1 

    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    genres = []
    x = 1
    menu()
    while x != '':
        x = input('Enter a genre number (ENTER to quit): ')
        if x.isdigit() == True:
            n = int(x)
            if n > len(Movie.GENRES):
                print('Error: input must be < {}'.format(len(Movie.GENRES)))
            elif genres.count(n) > 0:
                print('Error: genre already chosen')
            else:
                genres.append(n)
        elif x != '':
            print('Error: not a positive number')
        if genres == []:
            x = '0'
    genres.sort()
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """

    # a list to add the movies from the year 
    ymovies = [] 
    
    
    #for each movie in the text file movies 
    for movie in movies: 
        #if the movie year in the object, is equal to year inputed by user    
        if movie.year == year: 
            #add movie to the list 
            ymovies.append(movie)
    
    return ymovies 
        
        


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    #defining list for rmovies 
    rmovies = [] 
    
    #read through each line in text file movies 
    for movie in movies: 
        if movie.rating >= rating:
            rmovies.append(movie)
    
    
    return rmovies



def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = [] 
    
    for x in movies:
        for i in x.genres:
            if i == genre:
                gmovies.append(x)
    
    return gmovies

    


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    gmovies = [] 
    for x in movies:
        if x.genres == genres:
            gmovies.append(x)
    return gmovies
                
            
    


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    value = 0
    counts = []
    
    z = 0
    y = 0
    x = 0
    
    for y in range(0, len(Movie.GENRES), 1):
        while x < len(movies):
            while z < len(movies[x].genres):
                if movies[x].genres[z] == y:
                    value += 1
                z += 1
            x += 1
            z = 0
        counts.append(value)
        value = 0
        y += 1
        x = 0

    return counts
