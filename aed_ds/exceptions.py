class EmptyListException(Exception):
    def __init__(self):
        self.head = None

    def empty_list_exception(self, head):
        if self.head == None:
            raise Exception

class InvalidPositionException(Exception):
    def __init__(self):
        self.position = 0
        self.size = None  
    
    def invalid_position_exception(self, position):
        for position in range(0, self.size() -1):
            if position < 0 or position > self.size() -1:
                raise Exception
    
class NoSuchElementException(Exception):
    pass
    