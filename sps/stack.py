
#============================= Stack Operators =================================

class Stack:
    """Describe stack class"""
    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        """Push an item onto the stack"""
        self.items.append(item)      # append new item to the end of list
        return None

    def pop(self):
        """Pop the first item off the stack and return it"""
        if not stack:           # If the stack is empty
            err("pop: stack is empty")
            return None
        else:                   # The stack has at least one item
            return self.items.pop()  # Return the last item of the stack

    # Call this function when you encounter "len"
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)

    def clear(self):
        """Empty the stack"""
        self.items[:] = []
        return None

    def dup(self):
        """Duplicate the top item of the stack"""
        self.items.push(stack[-1])
        return None

    def exch(self):
        """Exchange the top two stack values"""
        first, second = pop(), pop()
        push(first)
        push(second)
        return None

    # Call this function when you encounter "stack"
    def print(self):
        """Display the contents of the stack, without modifying it"""
        for item in reversed(self.items):
            print(item)
        print('=======================')
        return None

    # Call this function when you encounter '='
    def peek(self):
        """Pop the top item off of the stack and print it"""
        print(self.items.pop())
        return None

