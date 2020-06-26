from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..exceptions import DuplicatedKeyException, NoSuchElementException, \
    EmptyDictionaryException, EmptyTreeException
from .nodes.binary_nodes import BinarySearchTreeNode
from ..lists.singly_linked_list import SinglyLinkedList
from ..lists.singly_linked_list_iterator import SinglyLinkedListIterator

class BinarySearchTree(OrderedDictionary, Tree):
    def __init__(self):
        self.num_elements = 0
        self.root = None
 
    # Returns the number of elements in the dictionary.
    def size(self):
        return self.num_elements

    # Returns true if the dictionary is full.
    def is_full(self):
        return False

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k):
        return self.get_value(self.root, k)

    def get_value(self, root, k):
        if root == None:
            raise NoSuchElementException()
        elif root.get_key() == k:
            return root.get_element()
        elif root.get_key() > k:
            return self.get_value(root.get_left_child(), k)
        else:
            return self.get_value(root.get_right_child(), k)                               

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v):
        self.root = self.insert_element(self.root, k, v)

    def insert_element(self, root, k, v):
        if root is None:
            root = BinarySearchTreeNode(k, v)
            self.num_elements += 1
        else:
            if root.get_key() == k:
                raise DuplicatedKeyException()
            elif root.get_key() > k:
                node = self.insert_element(root.get_left_child(), k, v)
                root.set_left_child(node)
            else:
                node = self.insert_element(root.get_right_child(), k, v)
                root.set_right_child(node)
        return root    
    
    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v):
        return self.update_element(self.root, k, v)

    def update_element(self, root, k, v):
        if root == None:
            raise NoSuchElementException()
        elif root.get_key() == k:
            root.set_element(v)
        elif root.get_key() > k:
            self.update_element(root.get_left_child(), k, v)
        else:
            self.update_element(root.get_right_child(), k, v)   
                
    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k):
        if self.root == None:
            return False
        atual = self.root
        father = self.root
        left_child = True
        while atual.get_key() != k:
            father = atual
            if k < atual.get_key():
                atual.left_child
                left_child = True
            else:
                atual = atual.right_child
                left_child = False
            if atual == None:
                return False
        if atual.left_child == None and atual.right_child == None:
            if atual == self.root:
                self.root = None
            else:
                if left_child:
                    father.left_child = None
                else:
                    father.right_child = None
        elif atual.right_child == None:
            if atual == self.root:
                self.root = atual.left_child
            else:
                if left_child:
                    father.left_child = atual.left_child
                else:
                    father.right_child = atual.left_child
        elif atual.left_child == None:
            if atual == self.root:
                self.root = atual.right_child
            else:
                if left_child:
                    father.left_child = atual.right_child
                else:
                    father.right_child = atual.right_child
        
    # Returns a List with all the keys in the dictionary.
    def keys(self):
        keys_list = SinglyLinkedList()
        self._keys(self.root, keys_list)
        return keys_list
    
    def _keys(self, root, list):
         if root != None:
            self._keys(root.get_left_child(), list)
            list.insert_last(root.get_key())
            self._keys(root.get_right_child(), list)

    # Returns a List with all the values in the dictionary.
    def values(self):
        values_list = SinglyLinkedList()
        self._values(self.root, values_list)
        return values_list

    def _values(self, root, list):
         if root != None:
            self._values(root.get_left_child(), list)
            list.insert_last(root.get_element())
            self._values(root.get_right_child(), list)
    
    # Returns a List with all the key value pairs in the dictionary.
    def items(self):
        items_list = SinglyLinkedList()
        self._items(self.root, items_list)
        return items_list

    def _items(self, root, list):
         if root != None:
            self._items(root.get_left_child(), list)
            list.insert_last(root)
            self._items(root.get_right_child(), list)
            
    # Returns an iterator of the elements in the dictionary
    def iterator(self):
        return SinglyLinkedListIterator(self)

    # Returns the element with the smallest key
    # Throws EmptyTreeException
    def get_min_element(self):
        if self.is_empty():
            raise EmptyTreeException()
        return self.get_min_node(self.root).get_element()

    def get_min_node(self, root):
        if root.get_left_child() is None:
            return root
        return self.get_min_node(root.get_left_child())    

    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_element(self):
        if self.is_empty():
            raise EmptyTreeException()
        return self.get_max_node(self.root).get_element()

    def get_max_node(self, root):
        if root.get_right_child() is None:
            return root
        return self.get_max_node(root.get_right_child())    

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self):
        if self.is_empty():
            raise EmptyTreeException()
        return self.root.get_element() 
            
    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self):
        if self.is_empty():
            raise EmptyTreeException()
        else:
            return self._height(self.root)

    def _height(self, root):
        if root == None:
            return 0
        else:
            left_height = self._height(root.get_left_child())
            right_height = self._height(root.get_right_child())
            if (left_height > right_height):
                return 1 + left_height
            else:
                return 1 + right_height                 
        
    # Returns True if the tree is empty
    def is_empty(self):
        return self.root == None     

    