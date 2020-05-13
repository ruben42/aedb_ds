from .tad_iterator import Iterator
from ..exceptions import *
from .nodes import SingleListNode

class SinglyLinkedListIterator(Iterator):
    def __init__(self):
        self.first_element = first_element
        self.next_element = next_element

    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
    def has_next(self):
        if self.first_element != None:
            return True
        else:
            return False        

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    def next(self):
        try:
            return self.next_element
        except:
            raise NoSuchElementException()    

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    def rewind(self):
        self.next_element = first_element

