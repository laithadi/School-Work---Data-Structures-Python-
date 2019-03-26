''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-31 
...................................................
'''

from Stack_array import Stack

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    item = []
    
    while source.is_empty() != True:
        item.append(source.pop())
        
    for x in item:
        source.push(x)
    
    return 
    
    

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack. 
    When finished, the contents of source1 and source2 are interlaced 
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty():
        target.push(source1.pop())
    while not source2.is_empty():
        target.push(source2.pop())
    return target

               



def has_balanced_brackets(string):
    """
    -------------------------------------------------------
    Determines if a string contains balanced brackets or not. Non-bracket
    characters are ignored. Uses a stack. Brackets include {}, [], (), <>.
    Use: balanced = has_balanced_brackets(string)
    -------------------------------------------------------
    Parameters:
        string - the string to test (str)
    Returns:
        balanced (int) -
            BALANCED if the brackets in string are balanced
            MISMATCHED if the brackets in string are mismatched
            MORE_RIGHT if there are more right brackets than left in string
            MORE_LEFT if there are more left brackets than right in string
    -------------------------------------------------------
    """
    right = 0
    left = 0
    
    s = Stack()
    
    for x in string:
        if s.is_empty() == True:
            s.push(x)
        elif s.peek() == '[' and x == ']' or s.peek() == '(' and x == ')' or s.peek() == '{' and x == '}' or s.peek() == '<' and x == '>':
            s.pop()
        else:
            s.push(x)
            
    if s.is_empty() == True:
        balanced = 0
    else:
        while s.is_empty() == False:
            x = s.pop()
            if x == '(' or x == '[' or x == '{' or x == '<':
                left += 1
            elif x == ')' or x == ']' or x == '}' or x == '>':
                right += 1
        if right > left:
            balanced = 2
        elif left > right:
            balanced = 1
        else:
            balanced = 3
            
    return balanced

# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    string = string.split(" ")
    r = Stack()
    
    for i in string:
        if i.isdigit():
            r.push(i)
        elif i in OPERATORS:
            if i == "+":
                r.push(float(r.pop()) + float(r.pop()))
            elif i == "-":
                x = float(r.pop())
                y = float(r.pop())
                r.push(y-x)
            elif i == "*":
                r.push(float(r.pop()) * float(r.pop()))
            elif i == "/":
                r.push(float(r.pop()) / float(r.pop()))
    answer = r.pop()      
    return answer


# Constants
BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    
    r = 1
    s_4 = Stack()
    string1 = string
    for x in ' ,.!?':
        string1 = string1.replace(x, '')
    string1 = string1.lower()
    if (len(string1) % 2) == 0:
        for x in string1:
            if s_4.is_empty() == True:
                s_4.push(x)
            else:
                y = s_4.pop()
                if x != y:
                    s_4.push(y)
                    s_4.push(x)
    else:
        half = (len(string1) / 2) + 0.5
        for x in string1:
            if r < half:
                s_4.push(x)
            elif r > half:
                y = s_4.pop()
                if x != y:
                    s_4.push(y)
            r += 1
    if s_4.is_empty() == True:
        palindrome = True
    else:
        palindrome = False
        
    return palindrome
    


















    

        
                        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            