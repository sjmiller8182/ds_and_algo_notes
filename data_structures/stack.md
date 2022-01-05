# Stack

Literal think of a stack of books.
That's what a stack is, a literal stack of things.
A stack follows the Last-In-First-Out (LIFO) principle.

* **push** refers to adding something on top of the stack.
* **pop** refers to removing the top element of the stack.
* **peak** refers to look at the top element of the stack with out removing it.

In python, a stack can be implemented with a `list`.
A stack can also be implement with a linked list.

**List Implementation**

```python
class Stack:
    """
    A list implementation of a stack
    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop(-1)  # same as pop(len(stack) - 1)
    
    def peak(self):
        return self.stack[-1]  # same as stack[len(stack) - 1]
```

**Linked List Implementation**

```python
from linkedlist import LinkedList, Node

class Stack:
    """
    A linked list implementation of a stack
    """

    def __init__(self):
        self.linkedlist = LinkedList()

    def push(self, value) -> None:
        self.linkedlist.push_head(Node(value))
    
    def pop(self):
        return self.linkedlist.pop_head().value
    
    def peak(self):
        return self.linkedlist.head.value
```

## Operations and Complexity

* push: O(1) ST
* pop: O(1) ST
* peak: O(1) ST
