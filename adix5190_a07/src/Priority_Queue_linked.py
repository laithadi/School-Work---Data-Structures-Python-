''' 
...................................................
CP164 - Data Structures 

Author: laith Adi 

ID: 170265190    

Email: Adil5190@mylaurier.ca

Updated: 2019-03-15 
...................................................
'''

from copy import deepcopy


class _PQ_Node:

    def __init__(self, value, _nelt):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the nelt node in the priority queue
        Use: node = _PQ_Node(value, _nelt)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _nelt - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._nelt = _nelt


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._count == 0


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """

        return self._count


    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        previous = None
        current = self._front
        new_node = _PQ_Node(value, current)
        
        if self._count == 0:
            self._front = new_node
            self._rear = self._front
            self._rear._nelt = None
        
        while current is not None and value >= current._value:
            previous = current
            current = current._nelt
        
        new_node = _PQ_Node(value, current)

        if current is None:
            self._rear = new_node
            self._rear._nelt = None
            
        if previous is None:
            self._front = new_node
        else:
            previous._nelt = new_node

        self._count += 1
        
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"

        value = deepcopy(self._front._value)
        self._front = self._front._nelt
        
        self._count -= 1
        
        return value


    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"

        value = deepcopy(self._front._value)
        
        return value

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """

        l = True
        target1 = Priority_Queue()
        target2 = Priority_Queue()
   
        while self._count > 0:
            if l:
                target1._move_front_to_rear(self)
                target1._count += 1
            else:
                target2._move_front_to_rear(self)
                target2._count += 1
               
            l = not l
   
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an elternal
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
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

        while self._front is not None:
            if int(self._front._value) >= key:
                target2._move_front_to_rear(self)
            else:
                target1._move_front_to_rear(self)
        while not self.is_empty():
            self.remove()
        
        return target1, target2


    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        is_s1 = True
        
        while not (source1.is_empty() and source2.is_empty()):
            if is_s1 and not (source1.is_empty()):
                self._move_front_to_rear(source1)
            elif not is_s1 and not (source2.is_empty()):
                self._move_front_to_rear(source2)
            
            is_s1 = not is_s1
        
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"


        l = Priority_Queue()

        for i in source:
            l.insert(i)
        for i in l:
            self.insert(i)
        while not source.is_empty():
            source.remove()
            
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"

        node = source._front
        source._count -= 1
        source._front = source._front._nelt
        
        if source._front is None:
            source._rear = None
        if self._rear is None:
            self._front = node
        else:
            self._rear._nelt = node
            
        node._nelt = None
        self._rear = node
        self._count += 1

        return
    
    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, indel = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_listNode)
            current - pointer to the node containing key (_listNode)
            indel - indel of the node containing key (int)
        -------------------------------------------------------
        """
        
        current = self._front
        previous = None
        indel = 0
        
        while current is not None and key != current._value:
            previous = current
            current = current._nelt
            indel += 1
            
        if current is None:
            indel = -1
            previous = None
            
        return previous, current, indel

    def __iter__(self):
        """
        USE FOR TESTING ONlY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the nelt value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._nelt
