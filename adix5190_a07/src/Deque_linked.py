''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-03-15 
...................................................
'''

# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._count == 0


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """

        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        node = _Deque_Node(value, None, self._front)
        
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._front._prev = node
            self._front = node
            
        self._count += 1
        
        return


    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        node = _Deque_Node(value, self._rear, None)
        
        if self._rear is None:
            self._front = node
            self._rear = node
        else:
            self._rear._next = node
            self._rear = node
        
        self._count += 1
        
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"

        k = deepcopy(self._front._value)
        
        previous, current, index = self._linear_search(k)
        
        if self._count == 1 and index != -1:
            value = deepcopy(self._front._value)
            self._front = None
            self._rear = None
            self._count = 0
        
        elif index != -1: 
            if previous is None:
                self._front = self._front._next
                value = deepcopy(current._value)
                self._count -= 1
            
            elif current._next is None:
                previous._next = current._next
                self._rear = previous
                value = deepcopy(current._value)
                self._count -= 1
            
            else:
                previous._next = current._next
                value = deepcopy(current._value)
                self._count -= 1
        else:
            value = None
        
        if self._front is not None:
            self._front._prev = None
        
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        key = deepcopy(self._rear._value)
        
        previous, current, index = self._linear_search(key)
        
        if self._count == 1 and index != -1:
            value = deepcopy(self._front._value)
            self._front = None
            self._rear = None
            self._count = 0
        
        elif index != -1: 
            if previous is None:
                self._front = self._front._next
                value = deepcopy(current._value)
                self._count -= 1
            
            elif current._next is None:
                previous._next = current._next
                self._rear = previous
                value = deepcopy(current._value)
                self._count -= 1
            
            else:
                previous._next = current._next
                value = deepcopy(current._value)
                self._count -= 1
        else:
            value = None
        
        if self._front is not None:
            self._front._prev = None
        
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"


        value = deepcopy(self._front._value)

        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"


        value = deepcopy(self._rear._value)

        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
        
        #couldnt figure it out 
    
    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        
        current = self._front
        previous = None
        index = 0
        
        while current is not None and key != current._value:
            previous = current
            current = current._next
            index += 1
            
        if current is None:
            index = -1
            previous = None
            
        return previous, current, index

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next