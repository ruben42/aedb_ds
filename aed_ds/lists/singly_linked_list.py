from .tad_list import List
from ..exceptions import *
from .nodes import SingleListNode
from .singly_linked_list_iterator import SinglyLinkedListIterator

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
        if self.head == None:
            count = 0
            return count
        while node:
            count += 1
            node = node.get_next()
        return count
        

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        try:
            return self.head
        except:
            raise EmptyListException()        

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        try:
            return self.tail
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
        node = self.head
        position = 0
        while position <= self.size() -1:
            if node.get_element() == element:
                return position
            node = node.get_next()
            position += 1
        return -1         

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        #node = SingleListNode(element, None)
        #self.head = node
        new_node = SingleListNode(element, None)
        new_node.next_node = self.head
        self.head = new_node    

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        new_node = SingleListNode(element, None)
        if self.head is None:
            self.head = new_node
            return self.head
        last = self.head
        while(last.next_node):
            last = last.next_node
        last.next_node = new_node    

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
        self.head = node.get_next()
        return node.get_element()      

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.head == None:
            raise EmptyListException()
            if self.tail == last_node:
                last_node = None
                return last_node
        #if self.is_empty():
            #raise EmptyListException()
        #node = self.tail
        #_node = None
        #current = self.head
        #while current:
            #if current.get_next() == node:
                #current.get_next(None)
                #self.tail = _node  
            #current = current.get_next()
        #return node.get_element()                          
    
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
        del self.head

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        return SinglyLinkedListIterator(self)
    