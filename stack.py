class StackIndexError(Exception):
    pass


class Stack():
    """Simple stack implementation using python"""
    def __init__(self, size):
        '''
        initialize stack and set stack size
        '''
        self.stack = list()
        self.size = size
        self.top = -1

    def isFull(self):
        '''Check if stack is full'''
        if self.top >= self.size - 1:
            return True
        return False

    def __str__(self):
        return "{0}".format(self.stack)

    def isEmpty(self):
        '''Check if stack is empty'''
        if self.top < 0:
            return True
        return False

    def push(self, x):
        '''Add element x to stack'''
        if self.isFull():
            raise StackIndexError("Stack if already Full")
            return False
        self.stack.append(x)
        self.top += 1
        return True

    def pop(self):
        '''pop last element from stack'''
        if self.isEmpty():
            raise StackIndexError("Stack if empty")
            return False
        data = self.stack[self.top]
        self.top -= 1
        self.stack = self.stack[:-1]
        return data

    def peek(self):
        '''View last element without popping'''
        if self.isEmpty():
            raise StackIndexError("Stack if empty")
            return False

        return self.stack[self.top]
