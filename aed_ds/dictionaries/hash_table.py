from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item 

import ctypes 

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.array_size = size
        self.num_elements = 0
        self.table = (self.array_size * ctypes.py_object)() # Array of pointers

        # Create an empty list for each table position
        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.array_size

    def get(self, k):
        if self.has_key() == True:
            return current_item.get_value()
        else:
            raise NoSuchElementException()    
    
    def insert(self, k, v):
        # Check if it has key
        if self.has_key(k):
            raise DuplicatedKeyException()

        ## Insert new item
        # Calculate the table index
        idx = self.hash_function(k) # O(1)
        # Create a new Item
        item = Item(k, v)
        # Insert the item in the colision list
        self.table[idx].insert_last(item)
        # Update the number of elements
        self.num_elements += 1    

    def update(self, k, v):
        if self.has_key() == True:
            current_item.set_value(v)
        else:
            raise NoSuchElementException()        

    def remove(self, k):
        if not self.has_key(k):
            raise NoSuchElementException()

        idx = self.hash_function(k)
        it = self.table[idx].iterator()
        b = 0 
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                current_item.remove(b)
            b += 1        

    def keys(self):
        keys_list = SinglyLinkedList()
        for i in range(self.array_size):
            it = self.table[i].iterator()
            while it.has_next():
                current_item = it.next()
                keys_list.insert_last(current_item.get_key())
        return keys_list        

    def values(self):
        values_list = SinglyLinkedList()
        for i in range(self.array_size):
            it = self.table[i].iterator()
            while it.has_next():
                current_item = it.next()
                values_list.insert_last(current_item.get_value())
        return values_list   
            
    def items(self):
        items_list = SinglyLinkedList()
        for i in range(self.array_size):
            it = self.table[i].iterator()
            while it.has_next():
                current_item = it.next()
                items_list.insert_last(current_item)
        return items_list   

    def hash_function(self, k):
        return sum([ord(c) for c in k]) % self.array_size

    def has_key(self, k):
        idx = self.hash_function(k) # O(1)    
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return True
        return False