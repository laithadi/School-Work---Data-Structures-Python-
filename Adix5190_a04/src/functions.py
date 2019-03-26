''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-10 
...................................................
'''
from Priority_Queue_array import Priority_Queue


def queue_is_identical(source1, source2):
    """
    ----------------
    Determines whether two given queues are identical. Entries of 
    source1 and source2 are compared and if all contents are identical
    and in the same order, returns True, otherwise returns False.
    Use: identical = queue_is_identical(source1, source2)
    ---------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        identical - True if source1 and source2 are identical, False otherwise. 
            source1 and source2 are unchanged. (boolean)
    ---------------
    """
    identical = True  
    while identical == True and source1.is_empty() != True:
        if source1.remove() != source2.remove():
            identical = False
            
    return identical 


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    
    target1 = Priority_Queue()
    target2 = Priority_Queue()
     
    while len(source) != 0:
        y = source.remove()
        if y > key:
            target1.insert(y)
        else:
            target2.insert(y) 
    
    return target1, target2
    