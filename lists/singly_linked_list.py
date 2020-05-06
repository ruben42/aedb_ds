from tad_list import List
import exceptions
import nodes
from tad_iterator import iterator

class Node:
    def __init__(data):
        self.data = data
        self.next = None

class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.tail = None

    # Returns true iff the list contains no elements.
    def is_empty(self):
        return self.head == None

    # Returns the number of elements in the list.
    def size(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        try:
            return self.head.data
        except:
            raise EmptyListException()        

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        try:
            return self.tail.data
        except:
            raise EmptyListException()           

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        count = 0
        node = self.head 
        while node: 
            if (count == position):
                return node.data
            
            node = node.next
            count += 1

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        count = 0
        node = self.head
        while node:
            if node.data == element:
                return count
            node = node.next
            count += 1
        return -1         

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        node = Node(element)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = self.head       

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        node = Node(element)
        self.tail.next = node
        if not self.head:
            self.head = self.tail
        self.tail = node    

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if position == 0:
            self.insert_first(element)
        elif position == self.size() - 1:
            self.insert_last(element)
        else:
            count = 0
            node = self.head
            while node:
                if count == position:
                    _node = Node(element)
                    _node.next = node.next
                    node.next = _node
                    return

        raise InvalidPositionException()                                              

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if self.is_empty():
            raise EmptyListException()
        node = self.head
        self.head = node.next
        return node.data      

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.is_empty():
            raise EmptyListException()
        node = self.tail
        _node = self.head
        while _node:
            if _node.next == node:
                _node.next = None
                self.tail = _node
            _node = _node.next
        return node.data                          
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        try:
            count = 0
            node = self.head
            while node:
                if count == position:
                    return node.data
                node = node.next
                count += 1
        except:
            raise InvalidPositionException()            
    
    # Removes all elements from the list.
    def make_empty(self):
        del self.data

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
    