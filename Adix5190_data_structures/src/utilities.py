''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-01-23 
...................................................
'''
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue
from Stack_array import Stack

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack, 
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        stack.push(source.pop())

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while stack.is_empty() == False:
        target.insert(0, stack.pop())
        
    
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and 
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    print('Test is empty?')
    print(stack.is_empty())
    print(array_to_stack(stack, source))
    print('Test is empty?')
    print(stack.is_empty())
    print('Test for peek value: ')
    print(stack.peek())
    print('Test for push value: ')
    stack.push(1)
    print('Test for peek value: ')
    print(stack.peek())
    print('Test for pop value: ')
    stack.pop()
    print('Test is empty?')
    print(stack.is_empty())
    print('Test for peek value: ')
    print(stack.peek())


#from lab 3 

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue, 
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        queue.insert(source.pop(0))
    
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    x = 0 
    while queue.is_empty() == False:
        target.insert(x, queue.remove())
        x += 1
    return 

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq, 
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        pq.insert(source.pop(0))
    
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    x = 0 
    while pq.is_empty() == False:
        target.insert(x, pq.remove())
        x += 1
    
        
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    -------------------------------------------------------
    """
    q = Queue()


    print('Test is empty?')
    print(q.is_empty())
    print(array_to_queue(q, a))
    print('Test is empty?')
    print(q.is_empty())
    print('Test for peek value: ')
    print(q.peek())
    print('Test for push value: ')
    q.insert(1)
    print('Test for peek value: ')
    print(q.peek())
    print('Test for pop value: ')
    q.remove()
    print('Test is empty?')
    print(q.is_empty())
    print('Test for peek value: ')
    print(q.peek())

    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Priority_Queue are tested for both empty and 
        non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print(pq.is_empty())
    print(array_to_pq(pq, a))
    print(pq.is_empty())
    print(pq.peek())
    a = pq.remove()
    print(pq.peek())
    pq.insert(a)
    print(pq.peek())
    print(pq.is_empty())

    return

from List_array import List
def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contents of source to list. At finish, source is empty.
    Last element in source is at rear of list, 
    first element in source is at front of list.
    Use: array_to_list(list, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        llist.append(source[0])
        source.pop(0)
    return
    
def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(llist)):
        target.append(llist.pop(0))
        
    return


def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    The methods of List are tested for both empty and 
    non-empty lists using the data in a:
    is_empty, insert, remove, append, index, __contains__,
    find, count, max, min, __getitem__, __setitem__
    Use: list_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    lst.is_empty()
    print('Insert Dark City|1998|Alex Proyas|7.8|0')
    lst.insert(1, a[1])
    lst.is_empty()
    print('contains Dark City|1998|Alex Proyas|7.8|0?')
    print(lst.__contains__('''Dark City|1998|Alex Proyas|7.8|0
'''))
    print('Appended Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
    lst.append(a[0])
    print('max')
    value = lst.max()
    print(value)
    print('min')
    value = lst.min()
    print(value)
    print('get item at index 1')
    print(lst.__getitem__(1))
    print('index 1 is Zulu|1964|Cy Endfield|7.8|9')
    lst.__setitem__(1, a[2])
    print('get item at index 1')
    print(lst.__getitem__(1))
    print('find 1')
    print(lst.find(1))
    print('index of Dark City|1998|Alex Proyas|7.8|0')
    i = lst.index(a[1])
    print(i)
    print('Count number of times Dark City|1998|Alex Proyas|7.8|0 shows up')
    number = lst.count(a[1])
    print(number)
    print('Remove Dark City|1998|Alex Proyas|7.8|0')
    lst.remove(a[1])
    print('Count number of times Dark City|1998|Alex Proyas|7.8|0 shows up')
    number = lst.count(a[1])
    print(number)

    return
