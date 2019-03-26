''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-11 
...................................................
'''

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#task 1 
def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ""
    for i in string:
        i = i.upper()
        for j in range(len(ALPHABET)):
            if i == ALPHABET[j]:
                estring += i.replace(ALPHABET[j], ciphertext[j])
                if i == " ":
                    estring += " "
            elif i == "\n":
                estring += "\n"
    return estring

    

# task 2

def shift(string, n):
      """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ""
    for i in string:
        i = i.upper()
        if i in ALPHABET:
            letter = ALPHABET.find(i.upper())
            letter = letter + n
            if letter > 25:
                letter -= 26
            estring += ALPHABET[letter]
            letter = 0
        else:
            estring += i
    return estring

#task 3
def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = True
    s1 = ''
    for i in s:
        if i.isalpha() or i.isdigit():
            s1 = s1 + i
    s = s1
    if len(s) % 2 == 0:
        l = int(len(s)/2)
        for i in range(1, l+1):
            s1 = s[i-1]
            s2 = s[len(s)-i]
            if s1 != s2:
                palindrome = False
    else:
        l = int(len(s)/2 - 0.5)
        i = 0
        for i in range(1, l+1):
            s1 = s[i-1]
            s2 = s[len(s)-i]
            if s1 != s2:
                palindrome = False
            i += 1
    return palindrome

#task 4 
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """ 
    
    if year % 4 == 0:
        if year % 400 == 0:
            leap_year = True 
        elif year % 100 != 0:
            leap_year = True 
        else:
            leap_year = False 
    else: 
        leap_year = False 
    
    return leap_year 


#task 5 
def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    if len(a) == 0:
        md = 0 
        return md
    c = [] 
    
    i = 1
        
    for x in a[0:-1]:
        #calculates the difference between the two numbers 
        d = abs(a[i] - x)
        #add the value to a list 
        c.append(d)
        
        #count i up by one to move to the next value 
        i += 1  
    md = max(c)
    return md
    



#task 6 
def transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """ 
    b = []
    row = len(a)
    cols = len(a[0])
    for c in range(cols):
        b_inner = []
        for r in range(row):
            b_inner.append(a[r][c])
        b.append(b_inner)
    return b

#task 7
def rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    Use: ra = rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of float)
    Returns:
        ra - the rotated 2D list of values (2D list of float)
    -------------------------------------------------------
    """
    ra = []
    b = []
    row = len(a)
    cols = len(a[0])
    for r in range(row - 1, -1, -1):
        b.append(a[r])
    for c in range(cols):
        ra_inner = []
        for r in range(row):
            ra_inner.append(b[r][c])
        ra.append(ra_inner)
    return ra

#task 8 
def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains 
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    for j in values:
        k = i + 1
        while k < len(values):
            if j == values[k]: # 1st value == 2nd value, ... 1st value == 15th value 
                values.pop(k) # remove 2nd/3rd/15th value
            else:
                k += 1
        i += 1
    print('Cleaned:', values)
    return
        
            
    
    
    

            
    
            
    
    