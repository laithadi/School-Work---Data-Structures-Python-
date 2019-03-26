''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-03-08 
...................................................
'''


# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_ListNode)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        b = True
        if self._count != 0:
            b = False
        return b
    
    def print_values(self):
        x = self._front
        while x:
            x._value = str(x._value)
            if x._value.endswith('\n') == True:
                print(x._value[:-2] + ', ', end = '')
            else:
                print(x._value + ', ', end = '')
            x = x._next
        print()
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        
        if self._count == 0:
            n = _SL_Node(value, None)
            self._rear = n
            self._front = n
            
        else:
            while current is not None and value >= current._value:
                previous = current
                current = current._next
            n = _SL_Node(value, current)
            if previous is None:
                self._front = n
            elif current is None:
                self._rear._next = n
                self._rear = n
            else:
                previous._next = n
            self._count+=1
            
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0
 
        while current is not None and current._value != key:
            previous = current
            current = current._next
            index += 1
 
        if current is None:
            index = -1
 
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, _ = self._linear_search(key)
        if current is None:
            value = None
        else:
            value = current._value
            self._count -= 1
            if previous is None:
                self._front = current._next
            else:
                previous._next = current._next
        if self._count == 0:
            self._rear = None
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        current = self._front
        value = current._value
        self._count -= 1
        self._front = current._next
        if self._count == 0:
            self._rear = None
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """
        value = self.remove(key)
        
        while value is not None:
            value = self.remove(key)
            
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)
 
        if current is not None:
            value = deepcopy(current._value)
        else:
            value = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = deepcopy(self._front._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _,_,i = self._linear_search(key)
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front
        if i < 0:
            i = self._count + i
        j = 0
        while j < i:
            current = current._next
            j += 1
        value = deepcopy(current._value)
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _,current,_ = self._linear_search(key)
        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        value = deepcopy(self._rear._value)
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"
        value = deepcopy(self._front._value)
        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        number = 0
        current = self._front
        while current is not None:
            if key == current._value:
                number += 1
            current = current._next
        return number

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        sl = []
        i = 0
        
        for i in self:
            if i not in sl:
                sl.append(i)
            else:
                self.remove(i)
        
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    new_node = _SL_Node(value, None)
                    if self._rear is None:
                        self._front = new_node
                        self._rear = new_node
                    else:
                        self._rear._next = new_node
                        self._rear = new_node
                    self._count += 1

            source1_node = source1_node._next
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                new_node = _SL_Node(value, None)
                if self._rear is None:
                    self._front = new_node
                    self._rear = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                self._count += 1
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                new_node = _SL_Node(value, None)
                if self._rear is None:
                    self._front = new_node
                    self._rear = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                self._count += 1

            source2_node = source2_node._next
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()

        while self._front is not None:
            if self._front._value < key:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        left = True

        while self._front is not None:

            if left:
                new_node = _SL_Node(self._value, None)
                if target1._rear is None:
                    target1._front = new_node
                    target1._rear = new_node
                else:
                    target1._rear._next = new_node
                    target1._rear = new_node
                target1._count += 1
            else:
                new_node = _SL_Node(self._value, None)
                if target2._rear is None:
                    target2._front = new_node
                    target2._rear = new_node
                else:
                    target2._rear._next = new_node
                    target2._rear = new_node
                target2._count += 1
            left = not left
        return target1, target2

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        
        if len(self) % 2 == 0:
            for i in range(0, len(self)//2):
                target1.insert(self[i])
            for i in range(len(self)//2, len(self)):
                target2.insert(self[i])
        else:
            for i in range(0, len(self)//2):
                target1.insert(self[i])
            for i in range(len(self)//2 + 1, len(self)):
                    target2.insert(self[i])
            target1.insert(self[len(self)//2])
        while len(self) != 0:
            self.pop(0)
        
        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = lst.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()

        while self._front is not None:
            if func(self._front._value) == True:
                new_node = _SL_Node(self._value, None)
                if target1._rear is None:
                    target1._front = new_node
                    target1._rear = new_node
                else:
                    target1._rear._next = new_node
                    target1._rear = new_node
                target1._count += 1
            else:
                new_node = _SL_Node(self._value, None)
                if target2._rear is None:
                    target2._front = new_node
                    target2._rear = new_node
                else:
                    target2._rear._next = new_node
                    target2._rear = new_node
                target2._count += 1
        return target1, target2
    
    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (iterative version)
        Use: b = l.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            other_node = other._front

            while source_node is not None and source_node._value == other_node._value:
                source_node = source_node._next
                other_node = other_node._next

            identical = source_node is None
        return identical

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if len(source1) == len(source2):
            i = 0
            while i < len(source1):
                new_node = _SL_Node(source1[i], None)
                if self._rear is None:
                    self._front = new_node
                    self._rear = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                self._count += 1
                new_node = _SL_Node(source2[i], None)
                self._rear._next = new_node
                self._rear = new_node
                self._count += 1
                i += 1
        elif len(source1) > len(source2):
            i = 0
            while i < len(source2):
                new_node = _SL_Node(source1[i], None)
                if self._rear is None:
                    self._front = new_node
                    self._rear = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                self._count += 1
                new_node = _SL_Node(source2[i], None)
                self._rear._next = new_node
                self._rear = new_node
                self._count += 1
                i += 1
            while i < len(source1):
                new_node = _SL_Node(source1[i], None)
                if self._rear is None:
                    self._front = new_node
                    self._rear = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                self._count += 1
                i += 1
        else:
            i = 0
            while i < len(source1):
                new_node = _SL_Node(source1[i], None)
                if self._rear is None:
                    self._front = new_node
                    self._rear = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                self._count += 1
                new_node = _SL_Node(source2[i], None)
                self._rear._next = new_node
                self._rear = new_node
                self._count += 1
                i += 1
            while i < len(source2):
                new_node = _SL_Node(source2[i], None)
                if self._rear is None:
                    self._front = new_node
                    self._rear = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                self._count += 1
                i += 1
        while len(source1) > 0:
            source1.pop(0)
        while len(source2) > 0:
            source2.pop(0)
        
        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        count = 0
        current = self._front
        previous = None
        
        previous, current, count = self._linear_search_r_aux(key, current, count, previous)

        return previous, current, count

    def _linear_search_r_aux(self, key, current, count, previous):
        
        if current is not None and current._value != key:
            previous = current
            count += 1
            previous, current, count = self._linear_search_r_aux(key, current._next, count, previous)
        else:
            if current is None:
                count = -1
            
        
        return previous, current, count

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        # your code here

        return

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """
        identical = True
        if self._count != rs._count:
            identical = False
        else: 
            self.identical_r_aux(self._front, rs._front, identical)

        return identical
    
    def identical_r_aux(self, current, rs_node, identical):
        
        if current is not None and current._value == rs_node._value:
            identical = self.identical_r_aux(current._next, rs_node._next, identical)
        else:
            identical = False
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front
        
        if not source2.is_empty():
            self.intersection_r_aux(source1_node, source2)
        
        return
    
    def intersection_r_aux(self, source1_node, source2):
        
        if source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self.append(value)

            self.intersection_r_aux(source1_node._next, source2)
            
        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """

        # your code here

        return

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front
        self.union_r_aux(source1_node)
        
        source2_node = source2._front
        self.union_r_aux(source2_node)
        
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _SL_Node(value, None)
        if self._rear is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1
        return
    
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
